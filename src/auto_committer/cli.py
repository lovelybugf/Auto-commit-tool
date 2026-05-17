"""
Interactive CLI for Git Auto Committer.
Provides a menu-driven terminal interface for all operations.
"""
import os
import sys
from datetime import datetime, timedelta

from auto_committer import __version__
from auto_committer.config import (
    DEFAULT_CONFIG, load_config, save_config,
    load_repos, add_repo, remove_repo,
    CONFIG_FILE, REPOS_FILE,
)
from auto_committer.scanner import find_git_repos, get_repo_info
from auto_committer.committer import create_commits_for_date_range, push_repo
from auto_committer.utils import (
    C, setup_encoding, clear_screen,
    print_banner, print_menu, print_separator,
    print_success, print_error, print_info, print_warn,
    prompt, pause,
)


# ============================================================
# MENU HANDLERS
# ============================================================

def handle_scan(cfg):
    """[1] Scan repos on drive."""
    clear_screen()
    print(f"\n  {C.CYAN}{C.BOLD}🔍 SCAN GIT REPOSITORIES{C.RESET}\n")

    default_path = cfg.get("scan_path", "D:\\")
    scan_path = prompt("Đường dẫn quét", default_path)
    depth = int(prompt("Độ sâu quét", str(cfg.get("max_depth", 2))))

    print(f"\n  {C.YELLOW}⏳ Đang quét {scan_path} ...{C.RESET}\n")

    repos = find_git_repos(scan_path, max_depth=depth, exclude_dirs=cfg.get("exclude_dirs"))

    if not repos:
        print_error("Không tìm thấy repo nào.")
        pause()
        return

    print(f"  {C.GREEN}{C.BOLD}📊 Tìm thấy {len(repos)} repositories:{C.RESET}\n")
    print(f"  {'#':<4} {'Repo':<40} {'Branch':<10} {'Remote':<8} {'README'}")
    print(f"  {'─'*4} {'─'*40} {'─'*10} {'─'*8} {'─'*6}")

    for i, repo in enumerate(repos, 1):
        info = get_repo_info(repo)
        remote_icon = f"{C.GREEN}✅{C.RESET}" if info["remote"] else f"{C.RED}❌{C.RESET}"
        readme_icon = f"{C.GREEN}📖{C.RESET}" if info["has_readme"] else f"{C.RED}❌{C.RESET}"
        display_path = repo if len(repo) <= 40 else "..." + repo[-37:]
        print(f"  {i:<4} {display_path:<40} {info['branch']:<10} {remote_icon:<8} {readme_icon}")

    # Ask to add to repos.txt
    print_separator()
    add_choice = prompt("Thêm repos vào danh sách? (a=tất cả / số=chọn / n=không)", "n")

    if add_choice.lower() == "a":
        for repo in repos:
            add_repo(repo)
        print_success(f"Đã thêm {len(repos)} repos vào repos.txt")
    elif add_choice.lower() != "n":
        try:
            indices = [int(x.strip()) for x in add_choice.split(",")]
            count = 0
            for idx in indices:
                if 1 <= idx <= len(repos):
                    add_repo(repos[idx - 1])
                    count += 1
            print_success(f"Đã thêm {count} repos vào repos.txt")
        except ValueError:
            print_error("Lựa chọn không hợp lệ.")

    pause()


def handle_manage_repos():
    """[2] Manage repos list."""
    while True:
        clear_screen()
        print(f"\n  {C.CYAN}{C.BOLD}📂 QUẢN LÝ DANH SÁCH REPOS{C.RESET}\n")

        repos = load_repos()

        if not repos:
            print_warn("Chưa có repo nào trong danh sách.")
            print_info(f"File: {REPOS_FILE}")
        else:
            print(f"  {C.GREEN}Có {len(repos)} repos trong danh sách:{C.RESET}\n")
            for i, r in enumerate(repos, 1):
                exists = f"{C.GREEN}✅{C.RESET}" if os.path.isdir(r) else f"{C.RED}❌ (không tồn tại){C.RESET}"
                print(f"  {C.YELLOW}[{i}]{C.RESET} {r}  {exists}")

        print(f"""
  {C.YELLOW}┌─────────────────────────────────┐
  │  [a] ➕ Thêm repo              │
  │  [d] 🗑️  Xóa repo              │
  │  [c] 🧹 Xóa repos không tồn tại│
  │  [0] ↩️  Quay lại               │
  └─────────────────────────────────┘{C.RESET}""")

        choice = prompt("Chọn", "0")

        if choice == "0":
            break
        elif choice.lower() == "a":
            path = prompt("Đường dẫn repo")
            if path and os.path.isdir(os.path.join(path, ".git")):
                if add_repo(path):
                    print_success(f"Đã thêm: {path}")
                else:
                    print_warn("Repo đã có trong danh sách.")
            elif path:
                print_error(f"'{path}' không phải là git repo hợp lệ.")
            pause()
        elif choice.lower() == "d":
            if repos:
                idx = prompt("Số thứ tự repo cần xóa")
                try:
                    idx = int(idx)
                    if 1 <= idx <= len(repos):
                        removed = repos[idx - 1]
                        remove_repo(removed)
                        print_success(f"Đã xóa: {removed}")
                    else:
                        print_error("Số không hợp lệ.")
                except (ValueError, TypeError):
                    print_error("Nhập số không hợp lệ.")
            pause()
        elif choice.lower() == "c":
            cleaned = 0
            for r in repos[:]:
                if not os.path.isdir(r):
                    remove_repo(r)
                    cleaned += 1
            print_success(f"Đã xóa {cleaned} repos không tồn tại.")
            pause()


def handle_commit(cfg, auto_push=False):
    """[3]/[4] Auto commit (optionally with push)."""
    clear_screen()
    action = "AUTO COMMIT + PUSH" if auto_push else "AUTO COMMIT"
    print(f"\n  {C.CYAN}{C.BOLD}📝 {action}{C.RESET}\n")

    # Get repos
    repos = load_repos()
    if not repos:
        print_warn("Chưa có repo nào trong repos.txt!")
        print_info("Hãy dùng [1] Scan hoặc [2] Quản lý để thêm repos trước.")
        pause()
        return

    # Show repos
    print(f"  {C.GREEN}Repos sẽ được commit ({len(repos)}):{C.RESET}")
    for i, r in enumerate(repos, 1):
        print(f"    {C.YELLOW}[{i}]{C.RESET} {r}")

    print_separator()

    # Date range
    print(f"  {C.BOLD}📅 Khoảng thời gian:{C.RESET}")
    days_input = prompt("Số ngày (hoặc nhập 'range' để nhập from-to)", "30")

    if days_input.lower() == "range":
        from_str = prompt("Ngày bắt đầu (YYYY-MM-DD)")
        to_str = prompt("Ngày kết thúc (YYYY-MM-DD)", datetime.now().strftime("%Y-%m-%d"))
        try:
            start = datetime.strptime(from_str, "%Y-%m-%d")
            end = datetime.strptime(to_str, "%Y-%m-%d")
        except (ValueError, TypeError):
            print_error("Định dạng ngày không hợp lệ!")
            pause()
            return
    else:
        try:
            days = int(days_input)
            start = datetime.now() - timedelta(days=days)
            end = datetime.now()
        except ValueError:
            print_error("Nhập số không hợp lệ!")
            pause()
            return

    # Commits per day
    min_c = int(prompt("Min commits/ngày", str(cfg.get("min_commits_per_day", 1))))
    max_c = int(prompt("Max commits/ngày", str(cfg.get("max_commits_per_day", 1))))

    # Preview
    total_days = (end - start).days + 1
    print_separator()
    print(f"  {C.BOLD}📋 PREVIEW:{C.RESET}")
    print(f"    📂 Repos:        {len(repos)}")
    print(f"    📅 Từ:           {start.strftime('%Y-%m-%d')}")
    print(f"    📅 Đến:          {end.strftime('%Y-%m-%d')}")
    print(f"    📆 Số ngày:      {total_days}")
    print(f"    📝 Commits/ngày: {min_c}-{max_c}")
    if auto_push:
        print(f"    🚀 Auto push:    {C.GREEN}BẬT{C.RESET}")
    print()

    confirm = prompt("Xác nhận thực hiện? (y/N)", "N")
    if confirm.lower() != "y":
        print_error("Đã hủy.")
        pause()
        return

    # Execute
    print_separator()
    total_success = 0
    total_fail = 0
    messages = cfg.get("commit_messages", DEFAULT_CONFIG["commit_messages"])

    for repo in repos:
        if not os.path.isdir(repo):
            print_error(f"Bỏ qua (không tồn tại): {repo}")
            continue

        info = get_repo_info(repo)
        readme_file = info.get("readme_file", "README.md")
        repo_name = os.path.basename(repo)

        print(f"\n  {C.BLUE}🔧 [{repo_name}]{C.RESET} {repo}")

        results = create_commits_for_date_range(
            repo, start, end,
            min_per_day=min_c, max_per_day=max_c,
            readme_file=readme_file, messages=messages
        )

        success = sum(1 for r in results if r["success"])
        fail = len(results) - success
        total_success += success
        total_fail += fail

        print(f"    {C.GREEN}✅ {success} commits{C.RESET} | {C.RED}❌ {fail} bỏ qua{C.RESET}")

        if auto_push and info.get("remote"):
            print(f"    {C.YELLOW}🚀 Đang push...{C.RESET}", end=" ")
            ok, err = push_repo(repo)
            if ok:
                print(f"{C.GREEN}OK{C.RESET}")
            else:
                print(f"{C.RED}LỖI: {err}{C.RESET}")

    # Summary
    print_separator()
    print(f"  {C.BOLD}{C.GREEN}📊 KẾT QUẢ:{C.RESET}")
    print(f"    ✅ Tổng commits thành công: {C.GREEN}{total_success}{C.RESET}")
    print(f"    ❌ Tổng bỏ qua:            {C.RED}{total_fail}{C.RESET}")
    pause()


def handle_settings(cfg):
    """[5] Settings."""
    while True:
        clear_screen()
        print(f"\n  {C.CYAN}{C.BOLD}⚙️  CÀI ĐẶT{C.RESET}\n")

        scan_path_val = cfg.get('scan_path', 'D:\\')
        print(f"  {C.YELLOW}[1]{C.RESET} Scan path:          {C.GREEN}{scan_path_val}{C.RESET}")
        print(f"  {C.YELLOW}[2]{C.RESET} Max depth:           {C.GREEN}{cfg.get('max_depth', 2)}{C.RESET}")
        print(f"  {C.YELLOW}[3]{C.RESET} Min commits/day:     {C.GREEN}{cfg.get('min_commits_per_day', 1)}{C.RESET}")
        print(f"  {C.YELLOW}[4]{C.RESET} Max commits/day:     {C.GREEN}{cfg.get('max_commits_per_day', 3)}{C.RESET}")
        print(f"  {C.YELLOW}[5]{C.RESET} Auto push:           {C.GREEN}{cfg.get('auto_push', False)}{C.RESET}")
        msg_count = len(cfg.get('commit_messages', []))
        print(f"  {C.YELLOW}[6]{C.RESET} Commit messages:     {C.GREEN}{msg_count} mẫu{C.RESET}")
        print(f"\n  {C.YELLOW}[s]{C.RESET} 💾 Lưu cài đặt")
        print(f"  {C.YELLOW}[0]{C.RESET} ↩️  Quay lại")

        choice = prompt("\nChọn mục cần thay đổi", "0")

        if choice == "0":
            break
        elif choice == "1":
            default_sp = cfg.get("scan_path", "D:\\")
            cfg["scan_path"] = prompt("Scan path mới", default_sp)
        elif choice == "2":
            cfg["max_depth"] = int(prompt("Max depth mới", str(cfg.get("max_depth", 2))))
        elif choice == "3":
            cfg["min_commits_per_day"] = int(prompt("Min commits/day", str(cfg.get("min_commits_per_day", 1))))
        elif choice == "4":
            cfg["max_commits_per_day"] = int(prompt("Max commits/day", str(cfg.get("max_commits_per_day", 3))))
        elif choice == "5":
            cfg["auto_push"] = not cfg.get("auto_push", False)
            state = "BẬT" if cfg["auto_push"] else "TẮT"
            print_info(f"Auto push: {state}")
        elif choice == "6":
            print(f"\n  {C.BOLD}Commit messages hiện tại:{C.RESET}")
            for i, m in enumerate(cfg.get("commit_messages", []), 1):
                print(f"    {i}. {m}")
            print_info("Chỉnh sửa trực tiếp trong config.json")
        elif choice.lower() == "s":
            save_config(cfg)
            print_success("Đã lưu cài đặt vào config.json")

        if choice in ["1", "2", "3", "4", "5"]:
            pause()

    return cfg


# ============================================================
# MAIN ENTRY POINT
# ============================================================

def auto_run(cfg):
    """Run fully automatically without interactive prompts."""
    print(f"\n  {C.CYAN}{C.BOLD}🚀 CHẠY TỰ ĐỘNG (AUTO MODE){C.RESET}\n")
    
    # 1. Scan and update repos
    scan_path = cfg.get("scan_path", "D:\\")
    depth = cfg.get("max_depth", 2)
    print(f"  {C.YELLOW}⏳ Đang quét tìm repos tại {scan_path} ...{C.RESET}")
    
    repos = find_git_repos(scan_path, max_depth=depth, exclude_dirs=cfg.get("exclude_dirs"))
    new_added = 0
    for repo in repos:
        if add_repo(repo):
            new_added += 1
            
    print(f"  {C.GREEN}✅ Đã tìm thấy {len(repos)} repos (Thêm mới {new_added}).{C.RESET}\n")
    
    # 2. Commit for all repos in repos.txt
    saved_repos = load_repos()
    if not saved_repos:
        print_warn("Không có repo nào để commit.")
        return 0
        
    start = datetime.now() - timedelta(days=1)
    end = datetime.now()
    
    min_c = cfg.get("min_commits_per_day", 1)
    max_c = cfg.get("max_commits_per_day", 3)
    auto_push = cfg.get("auto_push", False)
    messages = cfg.get("commit_messages", DEFAULT_CONFIG["commit_messages"])
    
    print(f"  {C.YELLOW}⏳ Đang tiến hành tạo commit cho {len(saved_repos)} repos...{C.RESET}")
    
    total_success = 0
    total_fail = 0
    
    for repo in saved_repos:
        if not os.path.isdir(repo):
            continue
            
        info = get_repo_info(repo)
        readme_file = info.get("readme_file", "README.md")
        
        results = create_commits_for_date_range(
            repo, start, end,
            min_per_day=min_c, max_per_day=max_c,
            readme_file=readme_file, messages=messages
        )
        
        success = sum(1 for r in results if r["success"])
        fail = len(results) - success
        total_success += success
        total_fail += fail
        
        if auto_push and info.get("remote") and success > 0:
            push_repo(repo)
            
    print_separator()
    print(f"  {C.BOLD}{C.GREEN}📊 KẾT QUẢ AUTO RUN:{C.RESET}")
    print(f"    ✅ Tổng commits thành công: {C.GREEN}{total_success}{C.RESET}")
    print(f"    ❌ Tổng bỏ qua/lỗi:        {C.RED}{total_fail}{C.RESET}")
    print(f"\n  {C.CYAN}🎉 Hoàn tất!{C.RESET}\n")
    return 0

def main():
    """Main interactive loop."""
    # Handle flags
    if len(sys.argv) > 1:
        flag = sys.argv[1].lower()
        if flag in ("--version", "-v"):
            print(f"Git Auto Committer v{__version__}")
            return 0
        elif flag in ("--auto", "-a"):
            setup_encoding()
            cfg = load_config()
            return auto_run(cfg)

    setup_encoding()
    cfg = load_config()

    while True:
        clear_screen()
        print_banner(__version__)

        # Quick status
        repos = load_repos()
        print(f"  {C.DIM}📂 Repos trong danh sách: {len(repos)} | 📄 Config: {CONFIG_FILE}{C.RESET}")

        print_menu()

        choice = prompt("Chọn chức năng", "0")

        if choice == "1":
            handle_scan(cfg)
        elif choice == "2":
            handle_manage_repos()
        elif choice == "3":
            handle_commit(cfg, auto_push=False)
        elif choice == "4":
            handle_commit(cfg, auto_push=True)
        elif choice == "5":
            cfg = handle_settings(cfg)
        elif choice == "0":
            print(f"\n  {C.CYAN}👋 Tạm biệt!{C.RESET}\n")
            break
        else:
            print_error("Lựa chọn không hợp lệ!")
            pause()

    return 0

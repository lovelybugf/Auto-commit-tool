"""
Git Auto Committer - Main CLI Tool
===================================
Scan git repos on drive D: and auto-commit with custom dates.

Usage:
    python main.py scan                          # List all git repos
    python main.py commit --days 30              # Commit to all repos for last 30 days
    python main.py commit --from 2026-01-01 --to 2026-04-30  # Custom date range
    python main.py commit --repo "D:\\myproject"  # Single repo only
    python main.py commit --days 7 --push        # Commit and push
"""
import sys
import os

# Fix Windows encoding for emoji support
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    os.environ["PYTHONIOENCODING"] = "utf-8"

import argparse
from datetime import datetime, timedelta

from scanner import find_git_repos, get_repo_info
from committer import create_commits_for_date_range, push_repo


def cmd_scan(args):
    """Scan and list all git repositories."""
    print(f"\n🔍 Scanning {args.path} for git repositories...\n")
    repos = find_git_repos(args.path, max_depth=args.depth)
    
    if not repos:
        print("❌ No git repositories found.")
        return
    
    for repo in repos:
        info = get_repo_info(repo)
        icon = "✅" if info["remote"] else "📁"
        readme = "📖" if info["has_readme"] else "❌"
        print(f"  {icon} {repo}")
        print(f"     Branch: {info['branch']} | Remote: {info['remote'] or 'local only'} | README: {readme}")
    
    print(f"\n📊 Found {len(repos)} repositories.\n")


def cmd_commit(args):
    """Create commits for repositories."""
    # Determine date range
    if args.from_date:
        start = datetime.strptime(args.from_date, "%Y-%m-%d")
    else:
        start = datetime.now() - timedelta(days=args.days)
    
    if args.to_date:
        end = datetime.strptime(args.to_date, "%Y-%m-%d")
    else:
        end = datetime.now()
    
    # Determine repos
    if args.repo:
        repos = [args.repo]
    else:
        print(f"\n🔍 Scanning {args.path} for git repositories...")
        repos = find_git_repos(args.path, max_depth=args.depth)
    
    if not repos:
        print("❌ No repositories found.")
        return
    
    print(f"\n📅 Date range: {start.strftime('%Y-%m-%d')} → {end.strftime('%Y-%m-%d')}")
    print(f"📂 Repositories: {len(repos)}")
    print(f"📝 Commits per day: {args.min_commits}-{args.max_commits}\n")
    
    if not args.yes:
        confirm = input("⚠️  Proceed? (y/N): ").strip().lower()
        if confirm != "y":
            print("❌ Cancelled.")
            return
    
    total_success = 0
    total_fail = 0
    
    for repo in repos:
        info = get_repo_info(repo)
        readme_file = info.get("readme_file", "README.md")
        print(f"\n🔧 Processing: {repo}")
        
        results = create_commits_for_date_range(
            repo, start, end,
            min_per_day=args.min_commits,
            max_per_day=args.max_commits,
            readme_file=readme_file
        )
        
        success = sum(1 for r in results if r["success"])
        fail = len(results) - success
        total_success += success
        total_fail += fail
        print(f"   ✅ {success} commits | ❌ {fail} skipped")
        
        if args.push and info.get("remote"):
            print(f"   🚀 Pushing to remote...")
            ok, err = push_repo(repo)
            if ok:
                print(f"   ✅ Push successful")
            else:
                print(f"   ❌ Push failed: {err}")
    
    print(f"\n{'='*50}")
    print(f"📊 Total: {total_success} commits created, {total_fail} skipped")
    print(f"{'='*50}\n")


def main():
    parser = argparse.ArgumentParser(
        description="🤖 Git Auto Committer - Auto commit to git repos with custom dates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--path", default="D:\\", help="Root path to scan (default: D:\\)")
    parser.add_argument("--depth", type=int, default=2, help="Max scan depth (default: 2)")
    
    sub = parser.add_subparsers(dest="command")
    
    # Scan command
    sub.add_parser("scan", help="Scan and list git repositories")
    
    # Commit command
    commit_p = sub.add_parser("commit", help="Create commits in repositories")
    commit_p.add_argument("--days", type=int, default=30, help="Number of past days (default: 30)")
    commit_p.add_argument("--from", dest="from_date", help="Start date YYYY-MM-DD")
    commit_p.add_argument("--to", dest="to_date", help="End date YYYY-MM-DD")
    commit_p.add_argument("--repo", help="Single repo path (skip scanning)")
    commit_p.add_argument("--min-commits", type=int, default=1, help="Min commits/day (default: 1)")
    commit_p.add_argument("--max-commits", type=int, default=1, help="Max commits/day (default: 1)")
    commit_p.add_argument("--push", action="store_true", help="Push after committing")
    commit_p.add_argument("-y", "--yes", action="store_true", help="Skip confirmation")
    
    args = parser.parse_args()
    
    if args.command == "scan":
        cmd_scan(args)
    elif args.command == "commit":
        cmd_commit(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

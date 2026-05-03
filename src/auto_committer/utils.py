"""
Utility helpers: ANSI colors, UI components, and terminal helpers.
"""
import os
import sys


# ============================================================
# ANSI COLOR CODES
# ============================================================

class Colors:
    """ANSI escape codes for terminal styling."""

    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BG_BLUE = "\033[44m"


# Convenience alias
C = Colors


# ============================================================
# TERMINAL HELPERS
# ============================================================

def setup_encoding():
    """Fix Windows encoding for emoji/unicode support."""
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        os.environ["PYTHONIOENCODING"] = "utf-8"
        # Enable ANSI escape codes on Windows
        os.system("")


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


# ============================================================
# UI COMPONENTS
# ============================================================

def print_banner(version):
    """Print the application banner with version."""
    banner = f"""
{C.CYAN}{C.BOLD}╔══════════════════════════════════════════════════════╗
║           🤖 GIT AUTO COMMITTER v{version:<20s}║
║        Production Commit Automation Tool              ║
╚══════════════════════════════════════════════════════╝{C.RESET}
"""
    print(banner)


def print_menu():
    """Print the main interactive menu."""
    menu = f"""
{C.YELLOW}{C.BOLD}  ┌─────────────────────────────────────┐
  │          📋 MAIN MENU               │
  ├─────────────────────────────────────┤{C.RESET}
  │  {C.GREEN}[1]{C.RESET} 🔍 Scan repos trên ổ đĩa       │
  │  {C.GREEN}[2]{C.RESET} 📂 Quản lý danh sách repos      │
  │  {C.GREEN}[3]{C.RESET} 📝 Auto commit                  │
  │  {C.GREEN}[4]{C.RESET} 🚀 Auto commit + Push            │
  │  {C.GREEN}[5]{C.RESET} ⚙️  Cài đặt                      │
  │  {C.GREEN}[0]{C.RESET} ❌ Thoát                         │
{C.YELLOW}  └─────────────────────────────────────┘{C.RESET}
"""
    print(menu)


def print_separator():
    """Print a visual separator line."""
    print(f"\n{C.DIM}{'─' * 55}{C.RESET}\n")


def print_success(msg):
    """Print a success message."""
    print(f"  {C.GREEN}✅ {msg}{C.RESET}")


def print_error(msg):
    """Print an error message."""
    print(f"  {C.RED}❌ {msg}{C.RESET}")


def print_info(msg):
    """Print an informational message."""
    print(f"  {C.CYAN}ℹ️  {msg}{C.RESET}")


def print_warn(msg):
    """Print a warning message."""
    print(f"  {C.YELLOW}⚠️  {msg}{C.RESET}")


def prompt(msg, default=None):
    """Prompt user for input with optional default value."""
    if default:
        text = f"  {C.MAGENTA}▶ {msg} [{default}]: {C.RESET}"
    else:
        text = f"  {C.MAGENTA}▶ {msg}: {C.RESET}"
    val = input(text).strip()
    return val if val else default


def pause():
    """Wait for user to press Enter."""
    input(f"\n  {C.DIM}Nhấn Enter để tiếp tục...{C.RESET}")

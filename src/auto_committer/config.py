"""
Configuration management: load, save, and default settings.
"""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
CONFIG_FILE = os.path.join(PROJECT_ROOT, "config.json")
REPOS_FILE = os.path.join(PROJECT_ROOT, "repos.txt")

DEFAULT_CONFIG = {
    "scan_path": "D:\\",
    "max_depth": 2,
    "exclude_dirs": [
        "$RECYCLE.BIN", "System Volume Information", "node_modules",
        ".venv", "venv", "__pycache__", "Recovery", "PerfLogs",
        "Windows", "Program Files", "Program Files (x86)", "ProgramData"
    ],
    "commit_messages": [
        "📝 Update README with daily activity log",
        "🔧 Refactor and improve documentation",
        "📚 Update project documentation",
        "✨ Daily maintenance update",
        "🗓️ Scheduled documentation refresh",
        "📋 Update project changelog",
        "🛠️ Routine project update",
        "📖 Enhance README content",
    ],
    "auto_push": False,
    "min_commits_per_day": 1,
    "max_commits_per_day": 3,
    "time_range_start": "09:00",
    "time_range_end": "21:00"
}


# ============================================================
# CONFIG FILE OPERATIONS
# ============================================================

def load_config():
    """Load config from config.json, fallback to defaults."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            # Merge with defaults for any missing keys
            for k, v in DEFAULT_CONFIG.items():
                if k not in cfg:
                    cfg[k] = v
            return cfg
        except Exception:
            pass
    return DEFAULT_CONFIG.copy()


def save_config(cfg):
    """Save config to config.json."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=4, ensure_ascii=False)


# ============================================================
# REPOS FILE OPERATIONS
# ============================================================

def load_repos():
    """Load repo paths from repos.txt."""
    if not os.path.exists(REPOS_FILE):
        return []
    with open(REPOS_FILE, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
    return [l.strip() for l in lines if l.strip() and not l.strip().startswith("#")]


def save_repos(repos):
    """Save repo paths to repos.txt."""
    with open(REPOS_FILE, "w", encoding="utf-8") as f:
        f.write("# Git Auto Committer - Danh sach repo\n")
        f.write("# Moi dong la 1 duong dan tuyet doi den repo\n")
        f.write("# File nay KHONG duoc push len GitHub\n\n")
        for r in repos:
            f.write(r + "\n")


def add_repo(path):
    """Add a repo path to repos.txt. Returns True if added."""
    repos = load_repos()
    path = os.path.abspath(path)
    if path not in repos:
        repos.append(path)
        save_repos(repos)
        return True
    return False


def remove_repo(path):
    """Remove a repo path from repos.txt. Returns True if removed."""
    repos = load_repos()
    path = os.path.abspath(path)
    if path in repos:
        repos.remove(path)
        save_repos(repos)
        return True
    return False

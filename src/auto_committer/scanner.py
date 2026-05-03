"""
Scanner module: discover git repositories on the filesystem.
"""
import os
import subprocess

from auto_committer.config import DEFAULT_CONFIG


def find_git_repos(scan_path="D:\\", max_depth=2, exclude_dirs=None):
    """Scan a path for directories containing .git folders.

    Args:
        scan_path: Root directory to start scanning from.
        max_depth: Maximum directory depth to traverse.
        exclude_dirs: Set of directory names to skip during scanning.

    Returns:
        List of absolute paths to git repositories found.
    """
    if exclude_dirs is None:
        exclude_dirs = set(DEFAULT_CONFIG["exclude_dirs"])
    else:
        exclude_dirs = set(exclude_dirs)

    repos = []
    scan_path = os.path.abspath(scan_path)

    def _scan(current_path, depth):
        if depth > max_depth:
            return
        try:
            entries = os.listdir(current_path)
        except (PermissionError, OSError):
            return
        if ".git" in entries:
            repos.append(current_path)
            return  # Don't scan inside a git repo for nested repos
        for entry in entries:
            if entry in exclude_dirs or entry.startswith("."):
                continue
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path):
                _scan(full_path, depth + 1)

    _scan(scan_path, 0)
    return repos


def get_repo_info(repo_path):
    """Get basic info about a git repository.

    Args:
        repo_path: Absolute path to the git repository.

    Returns:
        Dictionary with keys: path, branch, remote, has_readme, readme_file.
    """
    info = {"path": repo_path, "branch": "unknown", "remote": None, "has_readme": False}
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=repo_path, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            info["branch"] = result.stdout.strip() or "HEAD"

        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=repo_path, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            info["remote"] = result.stdout.strip()

        for name in ["README.md", "readme.md", "README.txt", "README"]:
            if os.path.exists(os.path.join(repo_path, name)):
                info["has_readme"] = True
                info["readme_file"] = name
                break
    except Exception:
        pass
    return info

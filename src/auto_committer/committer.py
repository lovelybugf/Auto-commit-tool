"""
Committer module: create git commits with custom dates.
"""
import os
import random
import subprocess
from datetime import timedelta

from auto_committer.config import DEFAULT_CONFIG


def update_readme(repo_path, commit_date, readme_file="README.md"):
    """Update or create README with a timestamped activity log entry.

    Args:
        repo_path: Absolute path to the git repository.
        commit_date: datetime object for the commit timestamp.
        readme_file: Name of the README file to update.

    Returns:
        Absolute path to the updated README file.
    """
    readme_path = os.path.join(repo_path, readme_file)

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    else:
        project_name = os.path.basename(repo_path)
        content = f"# {project_name}\n\nProject repository.\n"

    date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    marker = "<!-- auto-committer-log -->"
    if marker in content:
        content = content[:content.index(marker)]

    log_entry = (
        f"{marker}\n\n---\n\n"
        f"## 📅 Activity Log\n\n"
        f"| Date | Status |\n|------|--------|\n"
        f"| {date_str} | ✅ Updated |\n"
        f"\n> 🤖 Auto-maintained by Git Auto Committer\n"
    )
    content = content.rstrip() + "\n\n" + log_entry

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    return readme_path


def create_commit(repo_path, commit_date, message=None, readme_file="README.md", messages=None):
    """Create a git commit with a specific date.

    Args:
        repo_path: Absolute path to the git repository.
        commit_date: datetime object for the commit timestamp.
        message: Specific commit message (random if None).
        readme_file: Name of the README file to update.
        messages: List of possible commit messages to choose from.

    Returns:
        True if commit was created, False if no changes to commit.
    """
    if message is None:
        msg_list = messages or DEFAULT_CONFIG["commit_messages"]
        message = random.choice(msg_list)

    update_readme(repo_path, commit_date, readme_file)

    subprocess.run(
        ["git", "add", readme_file],
        cwd=repo_path, capture_output=True, text=True, encoding="utf-8", timeout=10
    )

    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=repo_path, capture_output=True, text=True, encoding="utf-8", timeout=10
    )
    if result.returncode == 0:
        return False  # No changes to commit

    date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    result = subprocess.run(
        ["git", "commit", "-m", message],
        cwd=repo_path, capture_output=True, text=True, encoding="utf-8", timeout=30, env=env
    )
    return result.returncode == 0


def create_commits_for_date_range(repo_path, start_date, end_date,
                                   min_per_day=1, max_per_day=1,
                                   readme_file="README.md", messages=None):
    """Create commits for each day in a date range.

    Args:
        repo_path: Absolute path to the git repository.
        start_date: Start date for commits.
        end_date: End date for commits.
        min_per_day: Minimum number of commits per day.
        max_per_day: Maximum number of commits per day.
        readme_file: Name of the README file to update.
        messages: List of possible commit messages.

    Returns:
        List of dicts with keys: date, success, repo.
    """
    results = []
    current = start_date
    while current <= end_date:
        num_commits = random.randint(min_per_day, max_per_day)
        for _ in range(num_commits):
            hour = random.randint(9, 21)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            commit_time = current.replace(hour=hour, minute=minute, second=second)
            success = create_commit(repo_path, commit_time, readme_file=readme_file, messages=messages)
            results.append({"date": commit_time.isoformat(), "success": success, "repo": repo_path})
        current += timedelta(days=1)
    return results


def push_repo(repo_path):
    """Push commits to remote origin.

    Args:
        repo_path: Absolute path to the git repository.

    Returns:
        Tuple of (success: bool, error_message: str).
    """
    result = subprocess.run(
        ["git", "push"],
        cwd=repo_path, capture_output=True, text=True, encoding="utf-8", timeout=60
    )
    return result.returncode == 0, result.stderr

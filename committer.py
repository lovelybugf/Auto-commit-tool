"""Module to create commits with custom dates."""
import os
import subprocess
import random
from datetime import datetime, timedelta


COMMIT_MESSAGES = [
    "📝 Update README with daily activity log",
    "🔧 Refactor and improve documentation",
    "📚 Update project documentation",
    "✨ Daily maintenance update",
    "🗓️ Scheduled documentation refresh",
    "📋 Update project changelog",
    "🛠️ Routine project update",
    "📖 Enhance README content",
]


def update_readme(repo_path, commit_date, readme_file="README.md"):
    """Update or create README with a timestamped entry."""
    readme_path = os.path.join(repo_path, readme_file)
    
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    else:
        project_name = os.path.basename(repo_path)
        content = f"# {project_name}\n\nProject repository.\n"

    date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Remove old auto-committer footer if exists
    marker = "<!-- auto-committer-log -->"
    if marker in content:
        content = content[:content.index(marker)]
    
    # Add new log entry
    log_entry = (
        f"{marker}\n"
        f"\n---\n\n"
        f"## 📅 Activity Log\n\n"
        f"| Date | Status |\n"
        f"|------|--------|\n"
        f"| {date_str} | ✅ Updated |\n"
        f"\n> 🤖 Auto-maintained by Git Auto Committer\n"
    )
    content = content.rstrip() + "\n\n" + log_entry

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    return readme_path


def create_commit(repo_path, commit_date, message=None, readme_file="README.md"):
    """Create a git commit with a specific date."""
    if message is None:
        message = random.choice(COMMIT_MESSAGES)
    
    # Update README
    update_readme(repo_path, commit_date, readme_file)
    
    # Stage changes
    subprocess.run(
        ["git", "add", readme_file],
        cwd=repo_path, capture_output=True, text=True, encoding="utf-8", timeout=10
    )
    
    # Check if there are staged changes
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=repo_path, capture_output=True, text=True, encoding="utf-8", timeout=10
    )
    if result.returncode == 0:
        return False  # No changes to commit
    
    # Commit with custom date
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
                                   readme_file="README.md"):
    """Create commits for each day in a date range."""
    results = []
    current = start_date
    
    while current <= end_date:
        num_commits = random.randint(min_per_day, max_per_day)
        for _ in range(num_commits):
            hour = random.randint(9, 21)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            commit_time = current.replace(hour=hour, minute=minute, second=second)
            
            success = create_commit(repo_path, commit_time, readme_file=readme_file)
            results.append({
                "date": commit_time.isoformat(),
                "success": success,
                "repo": repo_path
            })
        current += timedelta(days=1)
    
    return results


def push_repo(repo_path):
    """Push commits to remote."""
    result = subprocess.run(
        ["git", "push"],
        cwd=repo_path, capture_output=True, text=True, encoding="utf-8", timeout=60
    )
    return result.returncode == 0, result.stderr

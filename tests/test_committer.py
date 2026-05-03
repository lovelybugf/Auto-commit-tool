"""Unit tests for the committer module."""
import os
from datetime import datetime

from auto_committer.committer import update_readme


def test_update_readme_creates_file(tmp_path):
    """Test that update_readme creates a new README if none exists."""
    repo = tmp_path / "test-repo"
    repo.mkdir()

    commit_date = datetime(2026, 1, 15, 10, 30, 0)
    result = update_readme(str(repo), commit_date)

    assert os.path.exists(result)
    content = open(result, encoding="utf-8").read()
    assert "test-repo" in content
    assert "2026-01-15 10:30:00" in content
    assert "auto-committer-log" in content


def test_update_readme_preserves_content(tmp_path):
    """Test that update_readme preserves existing README content."""
    repo = tmp_path / "test-repo"
    repo.mkdir()

    readme = repo / "README.md"
    readme.write_text("# My Project\n\nSome important content.\n", encoding="utf-8")

    commit_date = datetime(2026, 3, 1, 14, 0, 0)
    update_readme(str(repo), commit_date)

    content = readme.read_text(encoding="utf-8")
    assert "# My Project" in content
    assert "Some important content." in content
    assert "2026-03-01 14:00:00" in content


def test_update_readme_replaces_old_log(tmp_path):
    """Test that update_readme replaces old auto-committer log."""
    repo = tmp_path / "test-repo"
    repo.mkdir()

    readme = repo / "README.md"
    old_content = (
        "# My Project\n\n"
        "<!-- auto-committer-log -->\n"
        "Old log entry\n"
    )
    readme.write_text(old_content, encoding="utf-8")

    commit_date = datetime(2026, 5, 1, 12, 0, 0)
    update_readme(str(repo), commit_date)

    content = readme.read_text(encoding="utf-8")
    assert "Old log entry" not in content
    assert "2026-05-01 12:00:00" in content
    assert content.count("auto-committer-log") == 1

"""Unit tests for the scanner module."""
import tempfile

from auto_committer.scanner import find_git_repos, get_repo_info


def test_find_git_repos_discovers_repos(tmp_path):
    """Test that find_git_repos finds directories with .git folders."""
    # Create a fake repo
    repo_dir = tmp_path / "my-repo"
    repo_dir.mkdir()
    (repo_dir / ".git").mkdir()

    repos = find_git_repos(str(tmp_path), max_depth=2)
    assert str(repo_dir) in repos


def test_find_git_repos_skips_excluded(tmp_path):
    """Test that excluded directories are skipped."""
    excluded = tmp_path / "node_modules"
    excluded.mkdir()
    (excluded / ".git").mkdir()

    repos = find_git_repos(str(tmp_path), max_depth=2, exclude_dirs={"node_modules"})
    assert str(excluded) not in repos


def test_find_git_repos_respects_depth(tmp_path):
    """Test that scanning respects max_depth."""
    # Create a deeply nested repo
    deep = tmp_path / "a" / "b" / "c" / "repo"
    deep.mkdir(parents=True)
    (deep / ".git").mkdir()

    # Should not find it with depth=2
    repos = find_git_repos(str(tmp_path), max_depth=2)
    assert str(deep) not in repos

    # Should find it with depth=4
    repos = find_git_repos(str(tmp_path), max_depth=4)
    assert str(deep) in repos


def test_find_git_repos_empty_directory(tmp_path):
    """Test scanning an empty directory returns empty list."""
    repos = find_git_repos(str(tmp_path), max_depth=2)
    assert repos == []


def test_get_repo_info_returns_dict():
    """Test that get_repo_info returns proper structure."""
    info = get_repo_info(tempfile.gettempdir())
    assert "path" in info
    assert "branch" in info
    assert "remote" in info
    assert "has_readme" in info

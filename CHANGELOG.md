# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-05-03

### Added

- **Interactive CLI** — Menu-driven terminal interface with ANSI colors and emoji
- **Repository Scanner** — Auto-scan drives for git repositories with configurable depth
- **Auto Committer** — Create commits with custom dates (`GIT_AUTHOR_DATE` & `GIT_COMMITTER_DATE`)
- **Repo Manager** — Add, remove, and clean repository list via `repos.txt`
- **Date Range Commits** — Support for specific date ranges or N days back
- **Randomized Commits** — Random commit times (9h–21h) and messages with emoji
- **Auto Push** — Optional automatic push to remote after committing
- **Configuration** — Persistent settings via `config.json`
- **Packaging** — Proper Python package with `pyproject.toml` and `src/` layout
- **CI/CD** — GitHub Actions for linting, testing, and automated releases
- **Documentation** — README, CHANGELOG, CONTRIBUTING, COMMIT_CONVENTION, LICENSE

### Project Structure

```
src/auto_committer/
├── __init__.py      # Package metadata & version
├── __main__.py      # Entry point for python -m
├── cli.py           # Interactive menu interface
├── scanner.py       # Git repo discovery
├── committer.py     # Commit creation engine
├── config.py        # Configuration management
└── utils.py         # UI helpers & ANSI colors
```

[1.0.0]: https://github.com/lovelybugf/Auto-commit-tool/releases/tag/v1.0.0

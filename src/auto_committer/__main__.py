"""
Entry point for `python -m auto_committer`.
"""
import sys

from auto_committer.cli import main


if __name__ == "__main__":
    sys.exit(main())

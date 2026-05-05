import sys
from pathlib import Path

if __name__ == "__main__":
	sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.cli import main


if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))

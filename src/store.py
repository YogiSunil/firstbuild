import json
from pathlib import Path


def load_tasks(path: Path) -> list[dict]:
    if not path.exists():
        return []

    raw = path.read_text(encoding="utf-8")
    return json.loads(raw)


def save_tasks(path: Path, tasks: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(tasks, indent=2), encoding="utf-8")

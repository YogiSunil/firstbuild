import json
from pathlib import Path

from src.store import load_tasks, save_tasks


def test_load_tasks_returns_empty_list_when_file_missing(tmp_path):
    path = tmp_path / "tasks.json"

    result = load_tasks(path)

    assert result == []


def test_save_then_load_roundtrip(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [{"id": 1, "description": "Buy milk", "status": "todo"}]

    save_tasks(path, tasks)
    loaded = load_tasks(path)

    assert loaded == tasks


def test_save_tasks_writes_valid_json(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [{"id": 1, "description": "Buy milk", "status": "todo"}]

    save_tasks(path, tasks)

    raw = path.read_text(encoding="utf-8")
    parsed = json.loads(raw)
    assert parsed == tasks

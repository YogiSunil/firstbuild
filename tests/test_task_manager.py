import pytest

from src.task_manager import add_task, list_tasks, mark_done


def test_add_task_creates_todo_task_with_id_and_description():
	tasks = []

	task = add_task(tasks, "Buy milk")

	assert task == {
		"id": 1,
		"description": "Buy milk",
		"status": "todo",
	}
	assert len(tasks) == 1


def test_add_task_increments_ids():
	tasks = []

	first = add_task(tasks, "First")
	second = add_task(tasks, "Second")

	assert first["id"] == 1
	assert second["id"] == 2


def test_list_tasks_returns_all_tasks_in_order():
	tasks = [
		{"id": 1, "description": "Buy milk", "status": "todo"},
		{"id": 2, "description": "Read docs", "status": "done"},
	]

	result = list_tasks(tasks)

	assert result == tasks


def test_mark_done_updates_status_to_done_for_matching_id():
	tasks = [
		{"id": 1, "description": "Buy milk", "status": "todo"},
	]

	mark_done(tasks, 1)

	assert tasks[0]["status"] == "done"


def test_mark_done_raises_for_missing_id():
	tasks = []

	with pytest.raises(KeyError):
		mark_done(tasks, 999)

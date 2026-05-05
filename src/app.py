import sys
from pathlib import Path

from src.store import load_tasks, save_tasks
from src.task_manager import add_task, delete_task, list_tasks, mark_done


def _usage() -> str:
	return "Usage: app.py [add <description> | list | done <id> | delete <id>]"


def main(argv: list[str], tasks: list[dict] | None = None, storage_path: Path | None = None) -> int:
	path = storage_path if storage_path is not None else Path("tasks.json")
	working_tasks = load_tasks(path) if tasks is None else tasks
	persist_changes = tasks is None

	if not argv:
		print(_usage(), file=sys.stderr)
		return 1

	command = argv[0]

	if command == "add":
		if len(argv) < 2:
			print("Error: description is required", file=sys.stderr)
			print(_usage(), file=sys.stderr)
			return 1
		description = " ".join(argv[1:])
		task = add_task(working_tasks, description)
		if persist_changes:
			save_tasks(path, working_tasks)
		print(f"Added task #{task['id']}: {task['description']}")
		return 0

	if command == "list":
		for task in list_tasks(working_tasks):
			print(f"#{task['id']} [{task['status']}] {task['description']}")
		return 0

	if command == "done":
		if len(argv) != 2:
			print("Error: done requires an id", file=sys.stderr)
			print(_usage(), file=sys.stderr)
			return 1
		try:
			task_id = int(argv[1])
			mark_done(working_tasks, task_id)
		except (ValueError, KeyError) as exc:
			print(f"Error: {exc}", file=sys.stderr)
			return 1
		if persist_changes:
			save_tasks(path, working_tasks)
		print(f"Marked #{task_id} as done")
		return 0

	if command == "delete":
		if len(argv) != 2:
			print("Error: delete requires an id", file=sys.stderr)
			print(_usage(), file=sys.stderr)
			return 1
		try:
			task_id = int(argv[1])
			delete_task(working_tasks, task_id)
		except (ValueError, KeyError) as exc:
			print(f"Error: {exc}", file=sys.stderr)
			return 1
		if persist_changes:
			save_tasks(path, working_tasks)
		print(f"Deleted #{task_id}")
		return 0

	print(f"Error: unknown command '{command}'", file=sys.stderr)
	print(_usage(), file=sys.stderr)
	return 1

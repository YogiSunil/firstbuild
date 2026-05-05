import sys

from src.task_manager import add_task, delete_task, list_tasks, mark_done


def _usage() -> str:
	return "Usage: app.py [add <description> | list | done <id> | delete <id>]"


def main(argv: list[str], tasks: list[dict]) -> int:
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
		task = add_task(tasks, description)
		print(f"Added task #{task['id']}: {task['description']}")
		return 0

	if command == "list":
		for task in list_tasks(tasks):
			print(f"#{task['id']} [{task['status']}] {task['description']}")
		return 0

	if command == "done":
		if len(argv) != 2:
			print("Error: done requires an id", file=sys.stderr)
			print(_usage(), file=sys.stderr)
			return 1
		try:
			task_id = int(argv[1])
			mark_done(tasks, task_id)
		except (ValueError, KeyError) as exc:
			print(f"Error: {exc}", file=sys.stderr)
			return 1
		print(f"Marked #{task_id} as done")
		return 0

	if command == "delete":
		if len(argv) != 2:
			print("Error: delete requires an id", file=sys.stderr)
			print(_usage(), file=sys.stderr)
			return 1
		try:
			task_id = int(argv[1])
			delete_task(tasks, task_id)
		except (ValueError, KeyError) as exc:
			print(f"Error: {exc}", file=sys.stderr)
			return 1
		print(f"Deleted #{task_id}")
		return 0

	print(f"Error: unknown command '{command}'", file=sys.stderr)
	print(_usage(), file=sys.stderr)
	return 1

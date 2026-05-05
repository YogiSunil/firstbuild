def _next_id(tasks: list[dict]) -> int:
	if not tasks:
		return 1
	return max(task["id"] for task in tasks) + 1


def add_task(tasks: list[dict], description: str) -> dict:
	task = {
		"id": _next_id(tasks),
		"description": description,
		"status": "todo",
	}
	tasks.append(task)
	return task


def list_tasks(tasks: list[dict]) -> list[dict]:
	return tasks

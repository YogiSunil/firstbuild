TODO_STATUS = "todo"


def _next_id(tasks: list[dict]) -> int:
	if not tasks:
		return 1
	return max(task["id"] for task in tasks) + 1


def _build_task(task_id: int, description: str) -> dict:
	return {
		"id": task_id,
		"description": description,
		"status": TODO_STATUS,
	}


def add_task(tasks: list[dict], description: str) -> dict:
	task = _build_task(_next_id(tasks), description)
	tasks.append(task)
	return task


def list_tasks(tasks: list[dict]) -> list[dict]:
	return tasks


def mark_done(tasks: list[dict], task_id: int) -> None:
	for task in tasks:
		if task["id"] == task_id:
			task["status"] = "done"
			return
	raise KeyError(f"Task id {task_id} not found")

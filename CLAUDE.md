# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

Python CLI task tracker built with a strict test-first workflow. All features must map to acceptance criteria in `spec.md`.

## Commands

```bash
# Setup
python -m venv .venv
.venv\Scripts\activate
pip install pytest

# Run all tests
pytest

# Run a single test
pytest tests/test_task_manager.py::test_add_task_creates_todo_task_with_id_and_description

# Run the CLI
python src/app.py add "Buy milk"
python src/app.py list
python src/app.py done 1
python src/app.py delete 1
```

## Architecture

The domain layer and CLI layer are deliberately separated:

- `src/task_manager.py` — pure functions that operate on an in-memory `list[dict]`. No I/O, no file access. Each function receives and mutates (or returns) the task list directly.
- `src/app.py` — CLI entry point responsible for loading tasks from JSON, calling domain functions, saving back to JSON, and formatting output. Currently a stub.

Task shape: `{"id": int, "description": str, "status": "todo" | "done"}`

`mark_done` raises `KeyError` for missing IDs — the CLI layer must catch this and exit non-zero.

## Workflow Conventions

- Write tests first, then implementation, then refactor.
- Do not add features outside `spec.md`.
- Keep functions small and behavior explicit.

## Commit Protocol

For each feature, create three commits in order:
1. Failing tests
2. Implementation to green
3. Refactor while tests stay green

Do not combine failing tests and implementation in the same commit.

## Testing Expectations

- New behavior must include tests.
- Invalid inputs must return non-zero exit behavior in CLI tests.
- Final handoff requires all tests passing.

## Definition of Done

1. Feature maps to an acceptance criterion in `spec.md`.
2. Tests are present and green.
3. Commit history shows red/green/refactor progression.

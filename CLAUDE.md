# CLAUDE.md

## Project Context

This repository is a Python CLI task tracker built with a strict test-first workflow.

## Tech Stack

- Python 3.11+
- pytest
- File storage via JSON in local filesystem

## Architecture Conventions

- `src/task_manager.py`: domain logic for add/list/complete/delete operations
- `src/app.py`: CLI command routing and output formatting
- `tests/`: tests grouped by module and feature

## Workflow Conventions

- Write tests first, then implementation, then refactor.
- Keep each commit focused on one workflow stage.
- Do not add features that are outside `spec.md`.
- Keep functions small and behavior explicit.

## Testing Expectations

- Run all tests with `pytest`.
- New behavior must include tests.
- Invalid inputs must return non-zero exit behavior in CLI tests.
- Final handoff requires all tests passing.

## Definition of Done

1. The feature maps to acceptance criteria in `spec.md`.
2. Tests are present and green.
3. Commit history shows red/green/refactor progression.

# /hook

Enable and verify local Claude hook behavior for this Python repository.

## Purpose

Set up a lightweight safety hook so every file edit gets an immediate Python syntax check.

## Hook Configuration

This project uses `.claude/settings.json` with a `PostToolUse` hook:

- Trigger: `Write|Edit`
- Action: run `python -m py_compile` against the edited file path
- Output: prints success or syntax error message

## Verification Steps

Run these checks after creating/updating hook settings:

```bash
python -m py_compile src/task_manager.py
python -m py_compile src/app.py
pytest -q
```

## Usage Notes

- Keep this hook fast; avoid long-running commands in `PostToolUse`.
- For full project checks, run `/audit` or `pytest -q` separately.
- If a file is not Python, the hook output can be ignored for that edit.

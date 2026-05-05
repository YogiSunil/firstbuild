# /audit

Run a Python-focused project audit for this repository and summarize results in a clear, actionable format.

## Scope

- Language/runtime: Python 3.11+
- Test runner: pytest
- Project type: CLI task tracker
- Key modules:
	- `src/task_manager.py`
	- `src/app.py`
	- `src/store.py`
	- `tests/`

## What To Check

1. Test health
- Run `pytest -q`.
- Report pass/fail count and failing test names (if any).

2. Spec alignment
- Compare implementation against `spec.md` quality gates and acceptance criteria.
- Identify any criteria not covered by tests.

3. Architecture boundaries
- Confirm domain logic remains in `src/task_manager.py`.
- Confirm persistence logic remains in `src/store.py`.
- Confirm CLI orchestration and error handling remain in `src/app.py`.

4. CLI behavior quality
- Verify commands: `add`, `list`, `done`, `delete`.
- Verify invalid input returns non-zero behavior.

5. Workflow evidence
- Check commit history for red/green/refactor sequencing.
- Highlight at least one example per feature cycle.

## Command Checklist

Run these commands during audit:

```bash
pytest -q
git status --short --branch
git log --oneline -n 20
```

## Output Format

Return results with these sections:

1. Summary
- Overall project health (green/yellow/red)

2. Findings
- Critical issues
- Important issues
- Nice-to-have improvements

3. Requirements Coverage
- V1.0 status
- V1.1 status
- V1.2 status

4. Recommended Next Actions
- 1 to 3 concrete steps with exact file targets

## Notes

- Keep recommendations Python-specific.
- Do not suggest JavaScript tooling for this project.
- Prefer small, test-backed changes.

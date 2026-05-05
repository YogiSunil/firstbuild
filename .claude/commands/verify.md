# /verify

Run the project verification pipeline and summarize outcomes.

## Pipeline

Execute this from the repository root:

```bash
python verify.py
```

The script runs four checks in this order:

1. Import check
- Verifies all modules under `src/` import successfully.

2. Lint check
- Runs `ruff check src tests`.

3. Test check
- Runs `pytest` and requires zero failures.

4. Coverage check
- Runs coverage reporting and requires total coverage of at least 80%.

## Reporting Rules

After execution, report:

1. Passed checks and failed checks.
2. For any failed check:
- Include the key output lines.
- Explain exactly what should be fixed.
3. If all checks pass:
- Confirm the verification pipeline is clean.

## Notes

- Run checks from project root so paths resolve correctly.
- Do not skip a check because an earlier one failed; report each check outcome.

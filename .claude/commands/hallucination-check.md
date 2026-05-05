# /hallucination-check

Scan the current working changes for known AI hallucination patterns documented in this project's CLAUDE.md.

## Steps

1. Run `git diff HEAD` to get all uncommitted changes.
2. If nothing is returned, run `git diff HEAD~1` to check the last commit.
3. Read the **Known AI Hallucination Patterns** section of `CLAUDE.md`.
4. For each documented pattern, check whether the diff contains an instance of it.

## Patterns To Check

1. Deprecated type aliases:
- Imports from `typing` using `Dict`, `List`, `Optional` instead of built-in `dict`, `list`, `str | None`.

2. Bare None typing:
- Function parameters typed as `def f(x: list = None)` instead of `def f(x: list | None = None)`.

3. Dead utility functions:
- Functions that are defined and tested but never called from the CLI layer.
- Check both definition sites and call sites.

4. subprocess tests hiding coverage:
- CLI tests that only use `subprocess.run` with no in-process unit tests for `cmd_*` functions or `build_parser()`.

5. Spec vs CLAUDE.md drift:
- Any behavior described in the diff that contradicts either `spec.md` or `CLAUDE.md`.

## Report Format

For each pattern, output:

- PASS (not found)
- FAIL (found, with `file:line` and the offending snippet)

End with one summary line:

- `<passed_count>/<total_count> patterns passed`

## Output Template

- Deprecated type aliases: PASS | FAIL - file:line - snippet
- Bare None typing: PASS | FAIL - file:line - snippet
- Dead utility functions: PASS | FAIL - file:line - snippet
- subprocess tests hiding coverage: PASS | FAIL - file:line - snippet
- Spec vs CLAUDE.md drift: PASS | FAIL - file:line - snippet
- Summary: X/5 patterns passed

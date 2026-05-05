import importlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "src"
THRESHOLD = 80


def run_command(args: list[str]) -> tuple[bool, str]:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    output = (completed.stdout or "") + (completed.stderr or "")
    return completed.returncode == 0, output.strip()


def import_check() -> tuple[bool, str]:
    failures: list[str] = []

    for file in sorted(SRC_DIR.glob("*.py")):
        module_name = f"src.{file.stem}"
        try:
            importlib.import_module(module_name)
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{module_name}: {exc}")

    if failures:
        return False, "\n".join(failures)

    return True, "All src modules imported successfully."


def lint_check() -> tuple[bool, str]:
    return run_command([sys.executable, "-m", "ruff", "check", "src", "tests"])


def test_check() -> tuple[bool, str]:
    return run_command([sys.executable, "-m", "pytest", "-q"])


def coverage_check() -> tuple[bool, str]:
    ok, output = run_command(
        [
            sys.executable,
            "-m",
            "pytest",
            "--cov=src",
            "--cov-report=term",
            "-q",
        ]
    )

    if not ok:
        return False, output

    match = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", output)
    if not match:
        return False, output + "\nCould not parse TOTAL coverage from pytest output."

    total = int(match.group(1))
    if total < THRESHOLD:
        return False, output + f"\nCoverage {total}% is below required {THRESHOLD}%."

    return True, output


def main() -> int:
    checks = [
        ("Import check", import_check),
        ("Lint check", lint_check),
        ("Test check", test_check),
        ("Coverage check", coverage_check),
    ]

    passed = 0
    total = len(checks)
    failed_details: list[tuple[str, str]] = []

    print("Verification pipeline")
    print("=" * 22)

    for name, fn in checks:
        ok, detail = fn()
        if ok:
            passed += 1
            print(f"[PASS] {name}")
        else:
            print(f"[FAIL] {name}")
            failed_details.append((name, detail))

    print("\nSummary")
    print("-" * 7)
    print(f"{passed}/{total} checks passed")

    if failed_details:
        print("\nFailure details")
        print("-" * 15)
        for name, detail in failed_details:
            print(f"\n{name} output:")
            print(detail if detail else "(no output)")
        return 1

    print("All verification checks passed. Pipeline is clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import pytest

from src.app import main


def test_add_command_appends_task_and_returns_zero(capsys):
    tasks = []

    code = main(["add", "Buy milk"], tasks)

    out = capsys.readouterr().out
    assert code == 0
    assert "Added task #1" in out
    assert len(tasks) == 1


def test_list_command_prints_current_tasks(capsys):
    tasks = [{"id": 1, "description": "Buy milk", "status": "todo"}]

    code = main(["list"], tasks)

    out = capsys.readouterr().out
    assert code == 0
    assert "#1" in out
    assert "Buy milk" in out


def test_done_command_marks_task_done(capsys):
    tasks = [{"id": 1, "description": "Buy milk", "status": "todo"}]

    code = main(["done", "1"], tasks)

    out = capsys.readouterr().out
    assert code == 0
    assert "Marked #1 as done" in out
    assert tasks[0]["status"] == "done"


def test_delete_command_removes_task(capsys):
    tasks = [{"id": 1, "description": "Buy milk", "status": "todo"}]

    code = main(["delete", "1"], tasks)

    out = capsys.readouterr().out
    assert code == 0
    assert "Deleted #1" in out
    assert tasks == []


@pytest.mark.parametrize("argv", [[], ["unknown"], ["done"], ["delete"]])
def test_invalid_commands_return_nonzero(argv, capsys):
    tasks = []

    code = main(argv, tasks)

    err = capsys.readouterr().err
    assert code == 1
    assert "Usage" in err or "Error" in err


def test_done_with_missing_id_returns_nonzero(capsys):
    code = main(["done", "999"], [])

    err = capsys.readouterr().err
    assert code == 1
    assert "Error" in err


def test_delete_with_missing_id_returns_nonzero(capsys):
    code = main(["delete", "999"], [])

    err = capsys.readouterr().err
    assert code == 1
    assert "Error" in err

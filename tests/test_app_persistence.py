from src.app import main


def test_add_command_persists_to_file_when_storage_path_given(tmp_path):
    path = tmp_path / "tasks.json"

    code = main(["add", "Write tests"], tasks=None, storage_path=path)

    assert code == 0
    assert path.exists()



def test_done_command_updates_persisted_task(tmp_path):
    path = tmp_path / "tasks.json"
    main(["add", "Write tests"], tasks=None, storage_path=path)

    code = main(["done", "1"], tasks=None, storage_path=path)

    assert code == 0
    list_code = main(["list"], tasks=None, storage_path=path)
    assert list_code == 0

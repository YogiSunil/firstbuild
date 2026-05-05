# Spec

## Product

Build a JavaScript command-line task tracker with persistent local storage.

## Core Features

- add task
- list tasks
- mark task done
- delete task

## Quality Gates

### QG-1 Test Suite Gate

How to invoke:

node --test

Success criteria:

- Command exits with status code 0.
- No failing tests are reported.

### QG-2 Add and List Gate

How to invoke:

node src/index.js add "Write tests"
node src/index.js list

Success criteria:

- `add` exits 0 and prints created task id.
- `list` exits 0 and output includes the added task text.

### QG-3 Complete and Delete Gate

How to invoke:

node src/index.js add "Temporary"
node src/index.js done 1
node src/index.js delete 1

Success criteria:

- `done 1` exits 0 and updates task status to done.
- `delete 1` exits 0 and removes the task.
- `done 999` and `delete 999` exit non-zero with clear error text.

## Acceptance Criteria

### AC-1 Add Task

Given no tasks exist
When I run `node src/index.js add "Buy milk"`
Then a task is saved with a unique integer id, description, and `todo` status

### AC-2 List Tasks

Given tasks already exist
When I run `node src/index.js list`
Then all tasks are displayed with id, status, and description

### AC-3 Mark Task Done

Given task id 1 exists with `todo` status
When I run `node src/index.js done 1`
Then task id 1 status changes to `done`

### AC-4 Delete Task

Given task id 1 exists
When I run `node src/index.js delete 1`
Then task id 1 is removed from storage

### AC-5 Invalid Done ID

Given no task exists with id 999
When I run `node src/index.js done 999`
Then the command exits non-zero and prints an error

### AC-6 Invalid Delete ID

Given no task exists with id 999
When I run `node src/index.js delete 999`
Then the command exits non-zero and prints an error

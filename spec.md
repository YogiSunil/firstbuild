# Spec

## App
CLI Task Tracker

## Features
- add task
- list tasks
- complete task
- delete task

## Quality Gates

1. pytest passes
2. add + list works
3. complete + delete works

## Acceptance Criteria

Given a task  
When I add it  
Then it is saved

Given tasks exist  
When I list  
Then I see all tasks

Given a task  
When I complete it  
Then status updates

Given a task  
When I delete it  
Then it is removed

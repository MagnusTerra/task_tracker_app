# Task CLI App

A simple task CLI application built with Python.

## Installation

You can install this package using pip:

```bash
pip install -e .
```

## Usage

```bash
task_cli -h
```

## Commands

```bash
task_cli list
```

```bash
task_cli add
```

```bash
task_cli update
```

```bash
task_cli delete
```

```bash
task_cli mark-in-progress
```

```bash
task_cli mark-done
```

## Examples

```bash
task_cli list
```

```bash
task_cli add -t "Task title" -desc "Task description" -s "in-progress"
```

```bash
task_cli update -i 1 -t "Task title" -desc "Task description" -s "in-progress"
```

```bash
task_cli delete -i 1
```

```bash
task_cli mark-in-progress -i 1
```

```bash
task_cli mark-done -i 1
```


https://roadmap.sh/projects/task-tracker

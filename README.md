# Sync Git, sync and update your local branch with remote branch without pain

## Requirements
1. A lazy programmer who has lots of projects
2. Python 3

## How do I use it?

1. Clone Sync Git project place it in your work directory

```bash
git clone https://github.com/navidesma/sync_git
```

2. Define your projects directory

In `main.py`:

```python
project_directories = [
    "project_one",
    "project_two",
]
```

Every time you want to sync your projects

In Windows run:

```bash
py main.py
```

In Linux run:

```bash
python3 main.py
```

# What does it do?

It will check all your projects for uncommited changes first,
then it will push your commits if your local branch is ahead of remote or pull from remote if your local branch is behind
if you have `ammended` commits it will let you know and you can decide for your self

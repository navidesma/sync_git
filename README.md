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

Create a file named `project_directories.py`.
<br>
`project_directories.example.py` is there for you to checkout.

In `project_directories.py`:

```python
project_directories = [
    # if it is not next to sync_git directory:
    ["..", "dir_name", "project_name"],
    
    # if it is inside multiple directories
    ["first_dir", "second_dir", "project_name"]
    
    # if it is next to sync_git just write:
    ["project_name"],
]
```
!!! IMPORTANT: sync_git checks path from the parent directory of sync_git not inside sync_git directory

## How to run it

Each time you want to sync your projects

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
<br>
If your local branch is ahead of remote it will push your commits,
<br>
If your local branch is behind remote it will pull from remote,
<br>
if you have `ammended` commits it will let you know and you can decide for yourself

from run_command import (
    run_command,
    check_clean_tree,
    check_if_branch_is_ahead_or_behind_or_diverged,
)

from project_directories import project_directories

for project_name in project_directories:
    run_command(
        action_name="check if working tree is clean",
        command="git status",
        project_name=project_name,
        action_func=check_clean_tree,
    )

    run_command(
        action_name="update remote",
        command="git remote update",
        project_name=project_name,
    )

    run_command(
        action_name="check if branch is ahead or behind or diverged",
        command="git status",
        project_name=project_name,
        action_func=check_if_branch_is_ahead_or_behind_or_diverged,
    )
    
print("\n Your projects are synced.")

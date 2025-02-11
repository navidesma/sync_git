from os.path import join
from os import getcwd
import subprocess
import re

from constants import (
    CLEAN_TREE_STRING,
    BRANCH_AHEAD,
    BRANCH_BEHIND,
    DIVERGED_BRANCH_REGEX,
    BRANCH_UP_TO_DATE,
)

base_dir = join(getcwd(), "..")


def print_status(*status):
    print("\n", *status, "\n")


class BreakTheLoop(Exception):
    pass


def check_clean_tree(output: str, project_path: list[str]):
    if CLEAN_TREE_STRING not in output:
        print_status(
            f"!!!!!!!!!!!!!!!!!\n{project_path[-1]} tree is not clean\n!!!!!!!!!!!!!!!!!"
        )
        raise BreakTheLoop


def run_command(
    command: str,
    action_name: str,
    project_path: list[str],
    action_func=None,
):
    command = subprocess.Popen(
        cwd=join(base_dir, *project_path),
        args=command,
        stdout=subprocess.PIPE,
        shell=True,
    )

    (output, err) = command.communicate()

    p_status = command.wait()

    if p_status != 0:
        print_status(
            "something went wrong in:\n", project_path[-1], f"\nwhen {action_name}\n"
        )
        raise Exception()

    output_str = str(output)

    if action_func is not None:
        action_func(output=output_str, project_path=project_path)


def check_if_branch_is_ahead_or_behind_or_diverged(
    output: str, project_path: list[str]
):
    if BRANCH_UP_TO_DATE not in output:
        if re.search(DIVERGED_BRANCH_REGEX, output):
            print_status(
                "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",
                project_path[-1],
                " is diverged:\n use git pull --rebase or git push -f origin <YOUR_BRANCH_NAME>",
                "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",
            )
            raise BreakTheLoop

        if BRANCH_AHEAD in output:
            print_status(project_path[-1], " is ahead, running git push...")
            run_command(
                action_name="running push action",
                command="git push --all",
                project_path=project_path,
            )

        if BRANCH_BEHIND in output:
            print_status(project_path[-1], " is behind, running git pull...")
            run_command(
                action_name="running pull action",
                command="git pull --all",
                project_path=project_path,
            )

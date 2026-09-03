#!/usr/bin/env python3

# Write basic ffuf commands here and place the functions in daveScout.py

import subprocess


def run_ffuf(cmd):
    print(cmd)


if __name__ == "__main__":
    """
    - Fill each option with the appropriate ffuf command
        - directories
        - vhost
        - parameters
    Use additional options as needed.
    """
    option = int(input("Enter an option for FFUF fuzzing: "))
    cmd = []

    if option == 1:
        cmd = ["fake"]

    if option == 2:
        cmd = ["fake"]

    if option == 3:
        cmd = ["fake"]

    run_ffuf(cmd)

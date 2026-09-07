#!/usr/bin/env python3

# Write basic ffuf commands here and place the functions in daveScout.py

import subprocess
import argparse


"""
 - Fill each option with the appropriate ffuf command
     - directories
     - vhost
        * DNS Records?
        * Define the differences between virtual hosts and subdomains.
     - parameters
        * GET requests fuzzing
        * POST requests fuzzing
        * Value fuzzing
 Use additional options as needed.
"""

def run_ffuf(cmd, args):
    command = []

    if args.dir or args.page or args.ext:
        fuzzLoc = args.target + '/FUZZ'
        command = ['ffuf', '-u', fuzzLoc]

    elif args.domains:
        print(args.domains)

    elif args.vhost:
        print(args.vhost)

    elif args.get:
        print(args.get)

    elif args.put:
        print(args.put)

    ## Defining wordlists locations
    dirs = '/usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt'
    ext = '/usr/share/seclists/Discovery/Web-Content/raft-large-extensions.txt'
    page = '/usr/share/seclists/Discovery/Web-Content/raft-large-files.txt'
    domains = '/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt'
    vhost = '/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt'
    get = '/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt'
    put = '/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt'

    if args.fuzz:
        if args.dir:
            command.extend(['-w', dirs])
        if args.ext:
            command.extend(['-w', ext])
        if args.page:
            command.extend(['-w', page])
        if args.domains:
            command.extend(['-w', domains])
        if args.vhost:
            command.extend(['-w', vhost])
        if args.get:
            command.extend(['-w', get])
        if args.put:
            command.extend(['-w', put])

    command.extend(['-t','100','-c'])



    result = subprocess.run(command)

    print('Exit code:', result.returncode)

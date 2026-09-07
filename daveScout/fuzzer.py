#!/usr/bin/env python3

# Write basic ffuf commands here and place the functions in daveScout.py

import argparse
import subprocess
from urllib.parse import urlparse, urlunparse

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
    fuzzLoc = ""

    if args.dir or args.page or args.ext:
        if args.dir:
            fuzzLoc = args.target + "/FUZZ"
        if args.page:
            extension = input("Pass in an extension for the page (Ex: .php )")
            fuzzLoc = args.target + "/FUZZ" + extension
        if args.ext:
            fuzzLoc = args.target + "indexFUZZ"
    elif args.domains:
        url = urlparse(args.target)
        fuzzLocNet = f"FUZZ.{url.netloc}"
        fuzzLoc = urlunparse(url._replace(netloc=fuzzLocNet))
    elif args.vhost:
        url = urlparse(args.target)
        host_header = f"FUZZ.{url.netloc}"
        command = ["ffuf", "-u", args.target, "-H", f"Host: {host_header}"]
    elif args.get:
        fuzzLoc = args.target + '?FUZZ=key'
    elif args.put:
        command = ["ffuf", "-u", args.target, "-X", "POST", "-d", "'id=FUZZ'", "-H", "'Content-Type: application/x-www-form-urlencoded'"]
    else:
        return



    if len(command) == 0:
        command = ["ffuf", "-u", fuzzLoc]

    ## Defining wordlists locations
    dirs = "/usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt"
    ext = "/usr/share/seclists/Discovery/Web-Content/raft-large-extensions.txt"
    page = "/usr/share/seclists/Discovery/Web-Content/raft-large-files.txt"
    domains = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt"
    vhost = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt"
    get = "/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt"
    put = "/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt"

    if args.fuzz:
        if args.dir:
            command.extend(["-w", dirs])
        if args.ext:
            command.extend(["-w", ext])
        if args.page:
            command.extend(["-w", page])
        if args.domains:
            command.extend(["-w", domains])
        if args.vhost:
            command.extend(["-w", vhost])
        if args.get:
            command.extend(["-w", get])
        if args.put:
            command.extend(["-w", put])

    command.extend(["-t", "100", "-c"])

    result = subprocess.run(command)

    print("Exit code:", result.returncode)

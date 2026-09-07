#!/usr/bin/python3

import argparse
from socket import *
import sys, time
from datetime import datetime

# Modules
from scanner import run_port_scan
from fuzzer import run_ffuf

"""
Goals:
    - Create a command parser in python | DAB implemented 7/1/26
    - Port scanner | DAB Implemented 7/X/26
    - Fuzzing | DAB 9/7/26
        - Web pages & directories
        - Paramter
        - Extension
        - vhost/subdomains
    - SQL inj
"""

BANNER = r"""
    ██████╗  █████╗ ██╗   ██╗███████╗██╗  ██╗ █████╗ ████████╗
    ██╔══██╗██╔══██╗██║   ██║██╔════╝██║  ██║██╔══██╗╚══██╔══╝
    ██║  ██║███████║██║   ██║█████╗  ███████║███████║   ██║
    ██║  ██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██║██╔══██║   ██║
    ██████╔╝██║  ██║ ╚████╔╝ ███████╗██║  ██║██║  ██║   ██║
    ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝

        DaveHat Scout Engine
        """

def main():
    # do not include .py in usage messages
    # Define the program description & Epilog message
    parser = argparse.ArgumentParser(
        prog="davescout",
        description="Enumeration scripts for penetration testing",
        epilog=f"{BANNER}\n\nThank you for using %(prog)s !!",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )



    # This is always required.
    targetArg = parser.add_argument_group("Target IP or URL - 10.10.10.10 or http://davehat.net ")
    targetArg.add_argument("target", type=str)


    # These are "Required" options
    # The user must pick one of these :
        # scanner or fuzzing
    scannerArg = parser.add_argument_group("Port Scanning option")
    scannerArg.add_argument("-s", "--scan", action="store_true")

    fuzzinArg = parser.add_argument_group("Fuzzing webpage option")
    fuzzinArg.add_argument("-f", "--fuzz", action='store_true')
    '''
    Fuzzing sub parser command options
    - directories
    - page/extension
       *
    - vhost/sub domain
       * DNS Records
       * Web application response
    - parameters
       * GET requests fuzzing
       * POST requests fuzzing
       * Value fuzzing
    '''
    fuzzinArg.add_argument("--dir", action="store_true", help="Fuzz directories")
    fuzzinArg.add_argument("--ext", type=str, help="Fuzz specific extensions (e.g., php, asp, aspx)")
    fuzzinArg.add_argument("--page", action="store_true", help="Fuzz pages")
    fuzzinArg.add_argument("--domains", action="store_true", help="Fuzz subdomains")
    fuzzinArg.add_argument("--vhost", action="store_true", help="Fuzz virtual hosts")
    fuzzinArg.add_argument("--get", action="store_true", help="Fuzz GET parameters")
    fuzzinArg.add_argument("--put", action="store_true", help="Fuzz PUT parameters")
    fuzzinArg.add_argument("--fs", action="store_true", help="Fuzz filter size")

    # target is stored in this variable.
    args = parser.parse_args()

    ## Calling scanner.py file to run operations
    if args.scan:
        run_port_scan(args.target, 1000)

    ## Calling a fuzzing script to run operations
    if args.fuzz:
        run_ffuf(args.target, args)



if __name__ == "__main__":
    #print(BANNER)
    main()

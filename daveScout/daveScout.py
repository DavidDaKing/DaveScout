#!/usr/bin/python3

import argparse
from socket import *
import sys, time
from datetime import datetime

# Modules
from scanner import run_port_scan

"""
Goals:
    - Create a command parser in python | DAB implemented 7/1/26
    - Port scanner 
    - Fuzzing (directory brute forcing)
    - Fuzzing 
        - Directory Traversal
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

def portScanner(target):

    return
    # # Not a lot of customization here...
    # try:
    #     # scan the ports from 1 to 65,535
    #     for port in range(1,65535):
    #         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         socket.setdefaulttimeout(0.2)
    #         result = s.connect_ex((target,port))
    #         if result == 0:
    #             print(f"Port {port} is open")
    #         s.close()
            
    # except KeyboardInterrupt:
    #     print("Bye!")
    
    # except socket.error:
    #     print("server is not responding.")
            
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
    
    # target is stored in this variable. 
    args = parser.parse_args()
        

    if args.scan:
        run_port_scan(args.target, 1000)
    
    

if __name__ == "__main__":
    #print(BANNER)
    main()
    

#!/usr/bin/python3

"""
Goals:
    - Create python code that uses nmap functionality -- check 6/4/26
    - Create python code that uses ARP requests
"""

import time

import nmap


# This is the easy way
def initFunc():
    target = "127.0.0.1"

    nm = nmap.PortScanner()
    nm.scan(target, "22-443")

    # Iterate through protocols
    for proto in nm[target].all_protocols():
        print(f"Protocol: {proto}")

        ports = sorted(nm[target][proto].keys())
        for port in ports:
            state = nm[target][proto][port]["state"]
            serv = nm[target][proto][port]["name"]
            print(f"Port: {port}\tState: {state}\tService: {serv}")


# Easy way complete


if __name__ == "__main__":
    banner = r"""
    ██████╗  █████╗ ██╗   ██╗███████╗██╗  ██╗ █████╗ ████████╗
    ██╔══██╗██╔══██╗██║   ██║██╔════╝██║  ██║██╔══██╗╚══██╔══╝
    ██║  ██║███████║██║   ██║█████╗  ███████║███████║   ██║
    ██║  ██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██║██╔══██║   ██║
    ██████╔╝██║  ██║ ╚████╔╝ ███████╗██║  ██║██║  ██║   ██║
    ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝

        DaveHat Scout Engine
        """

    print(banner)

    # Keep track of run time
    nmap_start_time = time.perf_counter()
    initFunc()
    end_nmap_time = time.perf_counter()

    nmap_exec_time = end_nmap_time - nmap_start_time

    print(f"nmap-python module took {nmap_exec_time:.4f} seconds to complete")

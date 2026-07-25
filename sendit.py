#!/usr/bin/python3

"""
Goals:
    - Create python code that uses nmap functionality -- check 6/4/26
        * Just as fast as nmap.. (Makes sense)
    - Create python code that uses Standard TCP stream sockets -- check 6/4/26
        ** STILL NOT FASTER THAN NMAP + WAY SLOWER
"""

import socket
import time
from concurrent.futures import ThreadPoolExecutor

import nmap

# global variable
target = "127.0.0.1"


# This is the easy way
def initFunc():
    nm = nmap.PortScanner()
    nm.scan(target, "1-65535")

    # Iterate through protocols
    for proto in nm[target].all_protocols():
        print(f"Protocol: {proto}")

        ports = sorted(nm[target][proto].keys())
        for port in ports:
            state = nm[target][proto][port]["state"]
            serv = nm[target][proto][port]["name"]
            print(f"Port: {port}\tState: {state}\tService: {serv}")


# ARP HOST DISCOVERY FUNCTION

def scan_single_port(givenTarget, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((givenTarget, port)) == 0
    except Exception:
        return False


def port_scanner_loop(givenTarget, max_ports=65535, workers=200, timeout=0.5):
    print(f"Scanning {givenTarget} on ports 1-{max_ports} with {workers} workers and {timeout}s timeout")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(scan_single_port, givenTarget, port, timeout): port for port in range(1, max_ports + 1)}

        for future in futures:
            port = futures[future]
            if future.result():
                print(f"    [!] Port {port} is OPEN!")


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

    option = int(input("Nmap or Raw TCP/IP packets (0, 1)"))

    print(option)
    # Keep track of run time

    if option == 0:
        nmap_start_time = time.perf_counter()
        initFunc()
        end_nmap_time = time.perf_counter()
        nmap_exec_time = end_nmap_time - nmap_start_time
        print(f"nmap-python module took {nmap_exec_time:.4f} seconds to complete")

    # Python time

    if option == 1:
        python_start_time = time.perf_counter()
        port_scanner_loop(target)
        python_end_time = time.perf_counter()
        python_exec_time = python_end_time - python_start_time
        print(
            f"Sending standard IPv4 TCP stream sockets took {python_exec_time:.4f} seconds to complete"
        )

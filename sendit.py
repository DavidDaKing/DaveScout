#!/usr/bin/python3

"""
Goals:
    - Create python code that uses nmap functionality -- check 6/4/26
        * Just as fast as nmap.. (Makes sense)
    - Create python code that uses Standard TCP stream sockets -- check 6/4/26
        ** STILL NOT FASTER THAN NMAP + WAY SLOWER
"""

import socket
import threading
import time

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


def scan_single_port(givenTarget, port):
    try:
        # This is the standard IPv4 TCP stream socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # sock.settimeout(1.0)
            # target being the global variable
            # port being an argument.
            result = sock.connect_ex((givenTarget, port))
            if result == 0:
                print(f"    [!] Port {port} is OPEN!")
    except Exception:
        pass


def port_scanner_loop(givenTarget):
    # Scan port from 1-65535

    MAX_PORTS = 65535

    threads = []

    for port in range(1, MAX_PORTS):
        print(port)
        thread = threading.Thread(
            target=scan_single_port, args=(givenTarget, str(port))
        )
        threads.append(thread)
        thread.start()

    # synchronize threads
    for thread in threads:
        thread.join()


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

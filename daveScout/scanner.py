#!/usr/bin/env python3

from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# helper function to scan a single port
# Run as a loop

# Citations : https://null-byte.wonderhowto.com/how-to/sploit-make-python-port-scanner-0161074/

def scan_port(host, port, timeout=0.5):
    try:
        with socket(AF_INET, SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except Exception:
        return False

# Host, ports should be passed in from the main function.

def run_port_scan(host, ports, workers=100, timeout=0.5):
    print(f"Scanning {host} on ports 1-{ports} with {workers} workers and {timeout}s timeout")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_port = {
            executor.submit(scan_port, host, port, timeout): port
            for port in range(1, ports + 1)
        }

        for future in as_completed(future_to_port):
            port = future_to_port[future]
            if future.result():
                print(f"[*] Port: {port} Open")

    print("Scan finished, Exiting scanner ( DaveHat )")
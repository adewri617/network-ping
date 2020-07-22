#!/usr/bin/env python3

import time
import socket

pings = 1
# stop pinging after 10 times
    # for pings in range(10):
# keep pinging
while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = b'test'
    addr = ("127.0.0.1", 12000)

    start = time.time()
    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print(f'{data} {pings} {elapsed}')
        pings += 1
    except socket.timeout:
        print('REQUEST TIMED OUT')
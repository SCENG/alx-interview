#!/usr/bin/python3

import sys

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status, count in sorted(status_counts.items()):
        print("{}: {}".format(status, count))

def parse_line(line):
    parts = line.strip().split(" ")
    if len(parts) != 9:
        return None, None
    ip_address = parts[0]
    status_code = parts[8]
    try:
        file_size = int(parts[7])
    except ValueError:
        return None, None
    return ip_address, (status_code, file_size)

def compute_metrics():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            ip_address, data = parse_line(line)
            if ip_address is None or data is None:
                continue
            status_code, file_size = data

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_counts)

compute_metrics()

#!/usr/bin/python3
"""
Stats

This script reads from stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), it prints these statistics from the beginning:
- Total file size: File size: <total size>
  where <total size> is the sum of all previous <file size> (see input format above)
- Number of lines by status code:
  possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
  if a status code doesn’t appear or is not an integer, don’t print anything for this status code
  format: <status code>: <number>
  status codes should be printed in ascending order
"""

import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interruption signal (CTRL + C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue

        try:
            ip_address = parts[0]
            date = parts[3][1:]
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        if status_code in status_counts:
            status_counts[status_code] += 1
        total_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

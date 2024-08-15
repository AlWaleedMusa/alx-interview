#!/usr/bin/python3
"Log stats"

import sys


def print_msg(status, total_size):
    """
    Method to print
    Args:
        status: dict of status codes
        total_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_size))
    for key, val in sorted(status.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_size = 0
code = 0
counter = 0
status = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_size += int(parsed_line[0])
                code = parsed_line[1]

                if code in status.keys():
                    status[code] += 1

            if counter == 10:
                print_msg(status, total_size)
                counter = 0

finally:
    print_msg(status, total_size)

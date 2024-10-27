#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

line list = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""


import sys
import signal
import os
import re


status_codes = {"200": 0, "301": 0,
                "400": 0, "401": 0,
                "403": 0, "404": 0,
                "405": 0, "500": 0}

counter = 0
total_size = 0


def print_stats():
    """ prints the stats for each status code """
    print(f"File size: {total_size}")
    for code in status_codes.keys():
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def handler(sig, frame):
    """ sigint handler for 'Ctrl-C' """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handler)

pattern = (r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
           r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
           r'"(GET /projects/\d+ HTTP/1\.1)" '
           r'(\d{3}) (\d+)$')


try:
    for line in sys.stdin:
        counter += 1
        match = re.match(pattern, line)
        if match:
            stat = line.split(" ")
            if stat[-2] in status_codes.keys():
                status_codes[stat[-2]] += 1
                total_size += int(stat[-1])
            else:
                continue
        if counter == 10:
            print_stats()
            counter = 0

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

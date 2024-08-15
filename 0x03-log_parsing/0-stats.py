#!/usr/bin/python3
"""Module for keeping the log stats"""


import sys


def print_log(fs, st_code):
    """Prints the file size and status code."""
    print("File size: {}".format(fs))
    for key, value in sorted(st_code.items()):
        print("{}: {}".format(key, value))


file_size = 0
time_elapsed = 0
status_dict = {}
try:
    for i in sys.stdin:
        list_obj = i.split(" ")
        time_elapsed += 1
        if time_elapsed <= 10:
            file_size += int(list_obj[-1])
            status_code = list_obj[-2]
            if status_code in status_dict:
                status_dict[status_code] += 1
            else:
                status_dict[status_code] = 1
        if (time_elapsed == 10):
            print_log(file_size, status_dict)
            time_elapsed = 0
finally:
    print_log(file_size, status_dict)

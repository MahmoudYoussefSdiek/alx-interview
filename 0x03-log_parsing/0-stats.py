#!/usr/bin/python3
"""
Script that takes in a log file and parses it line by line.
"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints statistics about the log file.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        count = status_codes[code]
        print(f"{code}: {count}")


def parse_line(line, total_size, status_codes):
    """
    Parses a line of the log file.
    """
    try:
        parts = line.split()
        if len(parts) >= 7:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size

            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_codes[status_code] = status_codes.get(
                    status_code, 0) + 1

        return total_size, status_codes
    except ValueError:
        return total_size, status_codes


def run():
    """
    main function
    """
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            total_size, status_codes = parse_line(
                line, total_size, status_codes)

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    run()

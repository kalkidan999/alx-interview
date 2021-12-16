#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
                code> <file size>
"""

import sys
code = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}
sum = 0


def print_stats():
    """
    Function that print stats about log
    """
    global sum

    print('File size: {}'.format(sum))
    stcdor = sorted(code.keys())
    for each in stcdor:
        if code[each] > 0:
            print('{}: {}'.format(each, code[each]))


if __name__ == "__main__":
    cnt = 0
    try:
        """ Iterate the standard input """
        for data in sys.stdin:
            try:
                fact = data.split(' ')
                """ If there is a status code """
                if fact[-2] in code:
                    code[fact[-2]] += 1
                """ If there is a length """
                sum += int(fact[-1])
            except Exception:
                pass
            """ Printing control """
            cnt += 1
            if cnt == 10:
                print_stats()
                cnt = 0
    except KeyboardInterrupt:
        print_stats()
        raise
    else:
        print_stats()

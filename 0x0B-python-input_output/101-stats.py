#!/usr/bin/python3
""" Module to print status code """
import sys


class Magic:
    """ Class to generate instances with dict and size"""
    def __init__(self):
        """ Init method """
        self.dic = {}
        self.size = 0

    def init_dic(self):
        """ Initialize dict """
        self.dic = {'200': 0,
                    '301': 0,
                    '400': 0,
                    '401': 0,
                    '403': 0,
                    '404': 0,
                    '405': 0,
                    '500': 0}

    def add_status_code(self, status):
        """ add repeated number to the status code """
        if status in self.dic:
            self.dic[status] += 1

    def print_info(self):
        """ print status code """
        print("File size: {}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] != 0:
                print("{}: {}".format(key, self.dic[key]))

    def signal_handler(self, sig, frame):
        """ Handle the signal """
        self.print_info()
        sys.exit(0)


if __name__ == "__main__":
    magic = Magic()
    magic.init_dic()
    nlines = 0

    for line in sys.stdin:
        try:
            list_line = [x for x in line.split(" ") if x.strip()]
            magic.add_status_code(list_line[-2])
            magic.size += int(list_line[-1].strip("\n"))
        except:
            pass

        nlines += 1

        if nlines % 10 == 0:
            magic.print_info()

    magic.print_info()

#!/usr/bin/python3
''' Module defines write_file function '''


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as wr_file:
        return wr_file.write(text)

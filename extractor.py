#!/usr/bin/env python

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='''A script that extracts contents from a csv file
            into an sqlite database''')
    parser.add_argument('csv_file', type=argparse.FileType('r'), help='Csv file to be imported')
    args = parser.parse_args()

    with args.csv_file as csv_file:
        for line in csv_file:
            print([value.strip() for value in line.split(',')])

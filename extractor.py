#!/usr/bin/env python

import argparse
import contextlib
import csv
import os
import sqlite3

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='''A script that extracts contents from a csv file
            into an sqlite database''')
    parser.add_argument('csv_file',
                        type=argparse.FileType('r'),
                        help='Csv file to be imported')
    args = parser.parse_args()

    with args.csv_file as csv_file:
        # When used as a context manager, a sqlite connection already commits
        # the transaction, yet it does not close it. That's why it is used
        # combined with contextlib.closing
        db_name = '{}.db'.format(os.path.basename(csv_file.name))
        with contextlib.closing(sqlite3.connect(db_name)) as conn:
            with conn as connection:
                rows = csv.reader(csv_file, skipinitialspace=True)

                cursor = connection.cursor()
                cursor.execute(""" CREATE TABLE IF NOT EXISTS person (
                                                time timestamp PRIMARY KEY,
                                                name varchar NOT NULL,
                                                age integer
                                            ); """)

                cursor.executemany('insert or ignore into person values (?,?,?)',
                                   rows)

                print('{} values inserted'.format(cursor.rowcount))

                entries = cursor.execute("select count(*) from person").fetchone()[0]
                print('Total of {} entries'.format(entries))

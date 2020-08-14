# ===============================================================
# Copyright 2020 IBM Corporation All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# ===============================================================


import json
from datetime import datetime


"""
  Function which ingests the json objects and prints lines in default view
"""
def parse_logs(file, transform):
    with open(file) as fin:
        for line in fin:
            parse_json_object(line, transform)




"""
  Function to parse json object and print only required values
"""
def parse_json_object(record, transform_ts):
    json_record_object = json.loads(record)
    line = json_record_object['_line']
    ts = json_record_object['_ts']
    if transform_ts:
        ts = transform_to_date(ts)
    print("{} : {}".format(ts, line))


def transform_to_date(ts):
    timestamp = int(ts)/1000
    # if you encounter a "year is out of range" error the timestamp
    # may be in milliseconds, try `ts /= 1000` in that case
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",
                    help="logs file")
    parser.add_argument("-t", "--transform",
                    help="transforms timestamp to date", action="store_true")
    args = parser.parse_args()
    parse_logs(args.file, args.transform)


if __name__ == "__main__":
    # execute only if run as a script
    main()

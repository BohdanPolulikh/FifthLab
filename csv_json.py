import csv
import argparse
import os
import json
from pprint import pprint


def main():
    parser = argparse.ArgumentParser(
        description='''
        This program convert csv-file
        to json.'''
    )
    parser.add_argument('-csv',
                        type=str, help='Path to CSV file')
    parser.add_argument('-json',
                        type=str, help='Path and name of JSON file')
    args = parser.parse_args()
    with open(os.path.join(args.csv, 'user_details.csv')) as f:
        read_csv = csv.DictReader(f)
        users = list(read_csv)
        for user in users:
            del user['password']

    with open(args.json, 'w') as f:
        json.dump(users, f)

    '''
    with open(args.json) as f:
        data = json.load(f)
    pprint(data)
    '''


if __name__ == '__main__':
    main()




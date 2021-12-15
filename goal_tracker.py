import pandas as pd
import argparse
import sys

def parse_input():
    parser = argparse.ArgumentParser(description="Simple goal tracker")

    subparsers = parser.add_subparsers(help='Sub-commands', required=True, dest='command')
    add_parser = subparsers.add_parser('add', help='Add new goal')
    complete_parser = subparsers.add_parser('get_complete', help='Get complete goals')
    active_parser = subparsers.add_parser('get_active', help='Get active goals')
    failed_parser = subparsers.add_parser('get_failed', help='Get failed goals')
    exit_parser = subparsers.add_parser('exit', help='Exit')

    add_parser.add_argument('desc', help='Description')
    add_parser.add_argument('amount', help='Amount of goal')


    args = parser.parse_args()
    command = args.subparser
    if command == 'add':
        # function for creating goal???
        # func(args['desc'], args['amount'])
        pass

    elif command == 'get_complete':
        # get_complete() -> dataframe with completed
        pass
    elif command == 'get_active':
        # get_complete() -> dataframe with active
        pass
    elif command == 'get_failed':
        # get_complete() -> dataframe with failed
        pass
    elif command == 'exit':
        exit()

def exit():
    sys.exit()

def main():
    parse_input()


if __name__ == '__main__':
    main()
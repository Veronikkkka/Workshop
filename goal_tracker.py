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

def read_data(path_to_file):
    """
    Returns a dataframe from a csv file.
    """
    d_f = pd.read_csv(path_to_file)
    return d_f

def file_updater(task, d_f, path_to_file):
    """
    Updates the file.
    """
    for i in d_f.index:
        line = d_f.iloc[i].squeeze()
        number_of_times = line["Number of times"]
        if line["Date"] == task:
            number_of_times = line["Number of times"] + 1
            if str(line["Number of times"]) in line["Date"]:
                d_f.at[i,"Success"] = "+"
            else:
                d_f.at[i,"Failure"] = "+"
        d_f.at[i,"Number of times"] = number_of_times
        d_f.update(line)
    d_f.to_csv(path_to_file)

        
def exit():
    sys.exit()

def main():
    parse_input()


if __name__ == '__main__':
    main()

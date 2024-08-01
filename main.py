import os  # Importing os module for interacting with the operating system
import time  # Importing time module to manage synchronization intervals
from datetime import datetime  # Importing datetime to generate timestamped log filenames
from sys import argv  # Importing argv from sys for command-line argument parsing
from pyfoldersync.sync import synchronize_folders  # Importing the synchronize_folders function
from pyfoldersync.logger import setup_logging, log_operation  # Importing the setup_logging function and log_operation function

VERSION = '1.0.0'

def print_help():
    help_message = '''usage: python main.py [options]

example: python main.py -s <source_folder_path> -r <replica_folder_path> -i <synchronization_interval_in_seconds>

options:
    -v, --version         show version
    -h, --help            show help

arguments:
    -s, --source          path to the source folder
    -r, --replica         path to the replica folder
    -i, --interval        synchronization interval in seconds
'''
    print(help_message)

def print_version():
    print(f'version {VERSION}')

def parse_arguments():
    args = { 'source': None, 'replica': None, 'interval': None }

    if '-h' in argv or '--help' in argv:
        print_help()
        exit()
    if '-v' in argv or '--version' in argv:
        print_version()
        exit()
    
    for i, arg in enumerate(argv):
        if arg in ('-s', '--source'):
            args['source'] = argv[i + 1]
        elif arg in ('-r', '--replica'):
            args['replica'] = argv[i + 1]
        elif arg in ('-i', '--interval'):
            args['interval'] = int(argv[i + 1])

    if not args['source'] or not args['replica'] or not args['interval']:
        print('Error: Missing required arguments.')
        print_help()
        exit()

    return args

def main():
    args = parse_arguments()

    # Create the logs directory if it does not exist
    os.makedirs('logs', exist_ok=True)
    
    # Generate a timestamped log filename
    log_filename = datetime.now().strftime('logs/%Y-%m-%d_%H-%M-%S.log')
    
    # Setup logging with the generated log filename
    setup_logging(log_filename)
    
    try:
        while True:
            try:
                # Synchronize the source and replica folders
                synchronize_folders(args['source'], args['replica'])
            except FileNotFoundError as e:
                log_operation(f'Error: {e}')
                print(f'Error: {e}')
                break
            
            # Wait for the specified interval before the next synchronization
            time.sleep(args['interval'])
    except KeyboardInterrupt:
        # Print a message when the user stops the synchronization
        print('Synchronization stopped by user')

if __name__ == '__main__':
    if len(argv) < 2:
        print('Try `python main.py -h or --help` for more information.')
    else:
        main()

# pyfoldersync

pyfoldersync is a file synchronization tool that keeps a replica folder synchronized with a source folder at specified intervals. It includes features such as logging and file integrity checks using MD5 hashes.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Description](#description)
- [Features](#features)
- [Running Tests](#running-tests)
- [TODO](#todo)
- [DONE](#done)

## Requirements

- [Python](https://www.python.org/)
- [Loguru](https://loguru.readthedocs.io/en/stable/)
- [Pytest](https://docs.pytest.org/en/stable/)

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/handbob/pyfoldersync.git
    cd pyfoldersync
    ```

2. Set up a virtual environment:
    ```
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source venv/bin/activate
      ```

4. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

## Description

### `main.py`

Manages command-line arguments, logging setup, and starts the synchronization process.

- **Functions**:
  - `parse_arguments()`: Parses command-line arguments.
  - `print_help()`: Displays the help message.
  - `print_version()`: Displays the script version.
  - `main()`: Sets up logging and starts the synchronization loop.

### `logger.py`

Sets up logging configurations and provides a function to log operations.

- **Functions**:
  - `setup_logging(log_file)`: Sets up the logging configuration.
  - `log_operation(message)`: Logs a message with INFO level.

### `sync.py`

Contains the core logic for synchronizing the source and replica folders.

- **Functions**:
  - `synchronize_folders(source, replica)`: Synchronizes the contents of the source folder with the replica folder.

### `test_logger.py`

Tests the logging setup and operations.

- **Functions**:
  - `setup_logger_environment()`: Sets up the logging environment for the test.
  - `test_log_operation()`: Tests the `log_operation` function to ensure it correctly logs messages.

### `test_sync.py`

Tests the folder synchronization functionality.

- **Functions**:
  - `setup_test_environment()`: Sets up a test environment with source and replica directories, and initializes test files.
  - `test_synchronization()`: Tests the `synchronize_folders` function by checking creation, updating, and deletion of files and directories.

### `test_utils.py`

Tests the utility function for calculating the MD5 hash of a file.

- **Functions**:
  - `calculate_md5(file_path, chunk_size=4096)`: Calculates the MD5 hash of a file.
  - `setup_file_environment()`: Creates a temporary test file for MD5 hash calculation.
  - `test_calculate_md5()`: Tests the `calculate_md5` function to ensure it correctly calculates the MD5 hash of the test file.

## Features

- Synchronizes files and directories from a source folder to a replica folder.
- Logs synchronization actions to a timestamped log file.
- Provides command-line interface for specifying source, replica, and synchronization interval.
- Handles file and directory creation, updating, and deletion.
- Configurable synchronization interval.
- Displays help and version information via command-line options.
- Handles errors for missing directories and provides user-friendly messages.
- Provides MD5 hash calculation for file integrity checks.

## Running Tests

To run the tests, you can use the `pytest` framework. Below are the commands to run individual test files:

- To run the logger tests:
  ```
  pytest -s tests/test_logger.py
  ```
- To run the synchronization tests:
  ```
  pytest -s tests/test_sync.py
  ```
- To run the MD5 utility tests:
  ```
  pytest -s tests/test_utils.py
  ```
## TODO

- [ ] Add unit tests for synchronization functions.
- [ ] Implement exclusion filters for specific files or directories.
- [ ] Add option for one-way or two-way synchronization.
- [ ] Enhance logging details with more specific operation messages.
- [ ] Provide a graphical user interface (GUI) for easier usage.

## DONE

- [x] Implement basic folder synchronization.
- [x] Set up logging configuration.
- [x] Calculate MD5 hash for file integrity.
- [x] Handle file and directory creation, updating, and deletion.
- [x] Parse command-line arguments for source, replica, and interval.

# pyfoldersync

pyfoldersync is a file synchronization tool that keeps a replica folder synchronized with a source folder at specified intervals. It includes features such as logging and file integrity checks using MD5 hashes.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Description](#descriptions)
- [Features](#features)

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

## Descriptions

### `utils.py`

Provides a utility function for calculating the MD5 hash of a file.

- **Functions**:
  - `calculate_md5(file_path, chunk_size=4096)`: Calculates the MD5 hash of a file.

### `logger.py`

Sets up logging configurations and provides a function to log operations.

- **Functions**:
  - `setup_logging(log_file)`: Sets up the logging configuration.
  - `log_operation(message)`: Logs a message with INFO level.

### `sync.py`

Contains the core logic for synchronizing the source and replica folders.

- **Functions**:
  - `synchronize_folders(source, replica)`: Synchronizes the contents of the source folder with the replica folder.

### `main.py`

Manages command-line arguments, logging setup, and starts the synchronization process.

- **Functions**:
  - `parse_arguments()`: Parses command-line arguments.
  - `print_help()`: Displays the help message.
  - `print_version()`: Displays the script version.
  - `main()`: Sets up logging and starts the synchronization loop.

## Features

- Synchronizes files and directories from a source folder to a replica folder.
- Logs synchronization actions to a timestamped log file.
- Provides command-line interface for specifying source, replica, and synchronization interval.
- Handles file and directory creation, updating, and deletion.
- Configurable synchronization interval.
- Displays help and version information via command-line options.
- Handles errors for missing directories and provides user-friendly messages.

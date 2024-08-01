# pyfoldersync

pyfoldersync is a file synchronization tool that keeps a replica folder synchronized with a source folder at specified intervals. It includes features such as logging and file integrity checks using MD5 hashes.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)

## Requirements

- [Python 3.x](https://www.python.org/)
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

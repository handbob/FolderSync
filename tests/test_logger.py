import os
import pytest
from pyfoldersync.logger import setup_logging, log_operation

@pytest.fixture
def setup_logger_environment():
    log_file = 'logs/test_logger.log'
    setup_logging(log_file)
    yield log_file
    if os.path.exists(log_file):
        os.remove(log_file)  # Clean up the log file after the test

def test_log_operation(setup_logger_environment):
    log_file = setup_logger_environment
    log_operation('test log entry')  # Log a test message

    with open(log_file, 'r') as f:
        logs = f.read()
    assert 'test log entry' in logs  # Check if the log message is in the log file

from loguru import logger  # Importing logger from the loguru library for logging
import sys  # Importing sys module to interact with the interpreter


def setup_logging(log_file):
    """
    Sets up the logging configuration.

    Args:
        log_file (str): The file where logs will be saved.
    """

    # Remove the default logger configuration
    logger.remove()

    # Add a file handler with a rotation of 10 MB
    logger.add(log_file, rotation='10 MB')

    # Add a standard error handler with INFO level logging
    logger.add(sys.stderr, level='INFO')


def log_operation(message):
    """
    Logs a message with INFO level.

    Args:
        message (str): The message to be logged.
    """

    # Log the provided message with INFO level
    logger.info(message)

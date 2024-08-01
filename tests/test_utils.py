import pytest
import tempfile
import os
import hashlib


def calculate_md5(file_path, chunk_size=4096):
    """
    Calculates the MD5 hash of a file.

    Args:
        file_path (str): The path to the file.
        chunk_size (int, optional): The size of each chunk read from the file. Default is 4096.

    Returns:
        str: The MD5 hash of the file.
    """
    hash_md5 = hashlib.md5()  # Create an MD5 hash object
    with open(file_path, 'rb') as f:  # Open the file in binary read mode
        for chunk in iter(lambda: f.read(chunk_size), b''):  # Read the file in chunks
            hash_md5.update(chunk)  # Update the hash object with the chunk
    return hash_md5.hexdigest()  # Return the hexadecimal digest of the hash


@pytest.fixture
def setup_file_environment():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file, 'w') as f:
            f.write('test content')
        print(f'Test file created at: {test_file}')
        yield test_file


def test_calculate_md5(setup_file_environment):
    test_file = setup_file_environment

    md5_hash = calculate_md5(test_file)
    print(f'Calculated MD5 hash using utility function: {md5_hash}')

    hash_md5 = hashlib.md5()
    with open(test_file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    direct_md5_hash = hash_md5.hexdigest()
    print(f'Calculated MD5 hash directly: {direct_md5_hash}')

    expected_md5_hash = '9473fdd0d880a43c21b7778d34872157'  # Correct MD5 hash for 'test content'
    print(f'Expected MD5 hash: {expected_md5_hash}')
    
    assert direct_md5_hash == expected_md5_hash
    assert md5_hash == expected_md5_hash

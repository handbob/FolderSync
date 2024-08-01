import hashlib  # Importing hashlib for hashing algorithms

def calculate_md5(file_path, chunk_size=4096):
    '''
    Calculates the MD5 hash of a file.
    
    Args:
        file_path (str): The path to the file.
        chunk_size (int, optional): The size of each chunk read from the file. Default is 4096.
        
    Returns:
        str: The MD5 hash of the file.
    '''
    hash_md5 = hashlib.md5()  # Create an MD5 hash object
    with open(file_path, 'rb') as f:  # Open the file in binary read mode
        for chunk in iter(lambda: f.read(chunk_size), b''):  # Read the file in chunks
            hash_md5.update(chunk)  # Update the hash object with the chunk
    return hash_md5.hexdigest()  # Return the hexadecimal digest of the hash

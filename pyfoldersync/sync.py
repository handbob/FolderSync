import os # Importing the os module to interact with the operating system
import shutil # Importing shutil for file operations
from pyfoldersync.logger import log_operation # Importing log_operation from the pyfoldersync.logger module


def synchronize_folders(source, replica):
    '''
    Synchronizes the contents of the source folder with the replica folder.
    
    Args:
        source (str): The source directory path.
        replica (str): The replica directory path.
    '''
    
    # Get the set of files and directories in the source folder
    source_files = set(os.listdir(source))
    
    # Get the set of files and directories in the replica folder
    replica_files = set(os.listdir(replica))

    # Loop through each file and directory in the source folder
    for file_name in source_files:
        # Get the full path of the source file or directory
        source_file = os.path.join(source, file_name)
        
        # Get the full path of the replica file or directory
        replica_file = os.path.join(replica, file_name)
        
        # Check if the source path is a directory
        if os.path.isdir(source_file):
            # Check if the directory does not exist in the replica folder
            if not os.path.exists(replica_file):
                # Create the directory in the replica folder
                os.makedirs(replica_file)
                
                # Log the creation of the directory
                log_operation(f'create directory: {replica_file}')
            
            # Recursively synchronize the subdirectory
            synchronize_folders(source_file, replica_file)
        else:
            # Check if the file does not exist in the replica folder
            if not os.path.exists(replica_file):
                # Copy the file to the replica folder
                shutil.copy2(source_file, replica_file)
                
                # Log the creation of the file
                log_operation(f'create file: {replica_file}')
            
            # Check if the source file is newer than the replica file
            elif os.path.getmtime(source_file) > os.path.getmtime(replica_file):
                # Copy the newer file to the replica folder
                shutil.copy2(source_file, replica_file)
                
                # Log the update of the file
                log_operation(f'update file: {replica_file}')

    # Loop through each file and directory in the replica folder
    for file_name in replica_files:
        # Check if the file or directory does not exist in the source folder
        if file_name not in source_files:
            # Get the full path of the replica file or directory
            replica_file = os.path.join(replica, file_name)
            
            # Check if the replica path is a directory
            if os.path.isdir(replica_file):
                # Remove the directory and its contents from the replica folder
                shutil.rmtree(replica_file)
                
                # Log the deletion of the directory
                log_operation(f'delete directory: {replica_file}')
            else:
                # Remove the file from the replica folder
                os.remove(replica_file) 
                
                # Log the deletion of the file
                log_operation(f'delete file: {replica_file}')

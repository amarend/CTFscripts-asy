import zipfile
import os
import re

def search_pattern_in_zip(zip_file_path, pattern):
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    # Open the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # List all files and directories in the zip file
        for file_info in zip_ref.infolist():
            # Recursively process files (ignore directories)
            if not file_info.is_dir():
                process_file(zip_ref, file_info, regex)

def process_file(zip_ref, file_info, regex):
    """Process a single file from the zip and search for the pattern"""
    # Read the file content
    with zip_ref.open(file_info.filename) as file:
        content = file.read().decode('utf-8', errors='ignore')  # Decode bytes to string
        # Search for the pattern in the file content
        if regex.search(content):
            print(f"Pattern found in file: {file_info.filename}")

def main():
    zip_file_path = input("Enter the path to the zip file: ")
    pattern = input("Enter the pattern to search for: ")
    search_pattern_in_zip(zip_file_path, pattern)

if __name__ == "__main__":
    main()

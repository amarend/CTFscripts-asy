import hashlib

def string_to_md5(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the string
    md5_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the MD5 hash
    return md5_hash.hexdigest()

# Example usage:
input_string = "Hello, World!"
md5_result = string_to_md5(input_string)
print(f"MD5 hash of '{input_string}': {md5_result}")

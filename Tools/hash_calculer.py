import hashlib  # Import the library to compute hashes

# Get user input for the password
passwd = input("Password: ").encode('utf-8')  # Ensure encoding to bytes

# Compute SHA-256 hash
hashsha256 = hashlib.sha256(passwd)  # Directly initialize with data

# Compute MD5 hash of the SHA-256 hexadecimal digest
hashmd5 = hashlib.md5(hashsha256.hexdigest().encode('utf-8'))

# Display results
print('sha256: ' + hashsha256.hexdigest())  # Print SHA-256 hash
print("flag{" + hashmd5.hexdigest() + "}")  # Print MD5 hash in flag format

import hashlib  # Import the hashlib library

hashmd5 = hashlib.md5()  
hashmd5.update('recuerdaquebase64NOescifrar'.encode('utf-8'))  # Convert to uppercase and encode before hashing
print("flag{" + hashmd5.hexdigest() + "}")  # Print the MD5 hash in flag format

# Layer-on-Layer-Encryption (LLE) 

# LLE with sha256 Using python3

from hashlib import sha256

inp = input("Enter something : ")   # Input 

hashSha256 = sha256(inp.encode('utf-8')).hexdigest()

keyLength = int(input("Enter key length : "))   # How many times to loop
x = 1

# Looping as many times as keyLength
while (x < keyLength):

    hashSha256 = sha256(hashSha256.encode('utf-8')).hexdigest()
    x = x+1

# Printing final hash value
print(hashSha256)

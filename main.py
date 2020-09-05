import hashlib
hash_hello = hashlib.sha256(b"HELLO").hexdigest()
print(hash_hello)
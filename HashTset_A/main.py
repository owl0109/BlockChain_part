import hashlib

hash_hello = hashlib.sha256(b"HELLO").hexdigest()
hash_hallo = hashlib.sha256(b"HALLO").hexdigest()
hash_helloworld = hashlib.sha256(b"HELLO WORLD").hexdigest()

print(hash_hello)
print(hash_hallo)
print(hash_helloworld)
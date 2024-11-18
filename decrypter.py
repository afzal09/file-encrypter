import sys
import base64
import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Decrypter():
    def __init__(self):
        self.file = open(sys.argv[1],"r")
        self.out_file = open('decrypted_file.txt','w+')
        self.password = sys.argv[2].encode("utf-8")
        self.salt = base64.b64decode(self.file.readline().strip())
    
    def decrypt(self):
        kdf = PBKDF2HMAC(algorithm=hashes.MD5(),length=32,salt=self.salt,iterations=64)
        key = base64.urlsafe_b64encode(kdf.derive(self.password))
        f = Fernet(key)
        for token in self.file:
            encrypted = token.encode("utf-8")
            self.out_file.write(f.decrypt(encrypted).decode("utf-8"))
        self.out_file.close()


if __name__ == '__main__':
    decrypter = Decrypter()
    decrypter.decrypt()
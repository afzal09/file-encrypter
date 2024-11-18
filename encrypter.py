import sys
import base64
import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Encrypter():
    def __init__(self):
        self.file = open(sys.argv[1],"r")
        self.out_file = open('encrypted_file.txt','w+')
        self.password = sys.argv[2].encode("utf-8")
        self.salt = os.urandom(16)
        self.out_file.write(base64.b64encode(self.salt).decode("utf-8")+"\n")
    
    def encrypt(self):
        kdf = PBKDF2HMAC(algorithm=hashes.MD5(),length=32,salt=self.salt,iterations=64)
        key = base64.urlsafe_b64encode(kdf.derive(self.password))
        f = Fernet(key)
        for line in self.file:
            token = f.encrypt(bytes(line,"utf-8"))
            encrypted = token.decode("utf-8")
            self.out_file.write(encrypted + "\n")
        self.out_file.close()


if __name__ == '__main__':
    encrypter = Encrypter()
    encrypter.encrypt()
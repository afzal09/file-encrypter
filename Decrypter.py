import sys
import base64
import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Decrypter():
    """
    This Decrypter class decrypts a text based file encrypted by the Encrypter class 
    this class constructor takes two parameters 
    first is the encrypted file, second is the password used to decrypt
    """
    def __init__(self,encryp_file,passwd):
        self.file = open(encryp_file,"r")
        self.out_file = open(f"{encryp_file.split('-')[0]}-decrypted_file.txt","w+")
        self.password =passwd.encode("utf-8")
        self.salt = base64.b64decode(self.file.readline().strip())
    
    def decrypt(self):
        kdf = PBKDF2HMAC(algorithm=hashes.MD5(),length=32,salt=self.salt,iterations=4096)
        key = base64.urlsafe_b64encode(kdf.derive(self.password))
        f = Fernet(key)
        try:
            for token in self.file:
                encrypted = token.encode("utf-8")
                self.out_file.write((f.decrypt(encrypted)).decode("utf-8"))
        except Exception as e:
            print('error:',e)
        finally:
            self.out_file.close()


if __name__ == '__main__':
    decrypter = Decrypter('encrypted_file.txt','0000')
    decrypter.decrypt()
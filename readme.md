# File-Encrypter 
## This Python app provides a utility to encrypt and decrypt text-based files securely using a password-based encryption mechanism. It consists leveraging PBKDF2-HMAC (password based key derivation function,Hash Message Authentication Code) and Fernet encryption schemes.

# Classes
## main app() class

## Encrypter() class 
### takes two parameters 1.file to encrypt 2. string based password

## DEcrypter() class
### takes two parameters 1.encrypted file 2.password

# Usage 
## install cryptography library run pip install cryptography

## to encrypt
### run `python app.py file_to_encrypt.txt password`

## to decrypt 
### run `python app.py encrypted_file.txt password`


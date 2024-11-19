# File-Encrypter 
This Python app provides a utility to encrypt and decrypt text-based files securely using a password-based encryption mechanism. It consists leveraging PBKDF2-HMAC (password based key derivation function,Hash Message Authentication Code) and Fernet encryption schemes.

# Classes
##### app(): is the main class that invokes the appropirate class

##### Encrypter(): takes two parameters 1.file to encrypt 2. string based password

##### Decrypter(): takes two parameters 1.encrypted file 2.password

# Usage 
install cryptography library, pyca/cryptography : [python cryptography](https://cryptography.io/en/latest/#)
run pip install cryptography

#### to encrypt

run `python app.py file_to_encrypt.txt password`

#### to decrypt 

run `python app.py encrypted_file.txt password`


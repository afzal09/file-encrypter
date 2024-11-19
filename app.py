import sys
from Encrypter import Encrypter
from Decrypter import Decrypter


class app():
    """ 
    An app class used to run specified operations
    """
    def __init__(self,operation,file,passwd):
        self.operation = operation
        self.file = file
        self.passwd = passwd

    def run(self):
        try:
            if self.operation == "encrypt":
                encrypter = Encrypter(self.file,self.passwd)
                encrypter.encrypt()
            elif self.operation == "decrypt":
                decrypeter = Decrypter(self.file,self.passwd)
                decrypeter.decrypt()
            else:
                raise ValueError(f"Invalid operation specified : {self.operation}")
        except Exception as e:
            print("error:",e)


if __name__ == '__main__':
    operation = sys.argv[1]
    file = sys.argv[2]
    passwd = sys.argv[3]
    app = app(operation=operation,file=file,passwd=passwd)
    app.run()
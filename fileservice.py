import os


class FileService():

    def __init__(self, file_path):
        self.file_path = file_path


    def write(self, content):
        print("write has been called")
        os.makedirs(os.path.dirname(self.file_path))
        mode = 'w'
        try:
            with open(self.file_path,mode) as f:
                f.write(content)
                print("hit write")
        except FileExistError as e:
            print("file already exists")
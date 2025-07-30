from quiz import Quiz
from fileservice import FileService

qa = {"What's the capital of France?":"Paris", "What's the capital of Poland?":"Warszawa"}

def main():
   # q = Quiz(qa)
   # q.main()

    fs = FileService("C:/Users/test.txt")
    fs.write("content inside the file")

    

if __name__ == "__main__":
    print("main has been called")
    main()


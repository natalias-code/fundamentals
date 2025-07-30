

class Quiz():
    qa = {}
    score = 0

    def __init__(self, qa):
        self.qa = qa 

    def answer_questions(self):

        for k in self.qa:
            answer = input(k)
            
            if answer == self.qa[k]:
                print("correct")

    def verifyAge(self,age):
        if age >= 18:
            print("access granted")
        else:
            print("access denied")
            


    def main(self):
        # user_age = float(input("input your age here:"))
        # verifyAge(user_age)
        self.answer_questions()


class Quiz():

    def __init__(self, qa):
        self.qa = qa
        self.correct_answers = set()
        self.incorrect_answers = set()

    def answer_questions(self):

        for k in self.qa:
            answer = input(k)
            
            if answer == self.qa[k]:
                print("correct")
                self.correct_answers.add(answer)
                print(self.correct_answers)
                counter = len(self.correct_answers)
                print(f"congratulations you got {counter} right!")
            else:
                self.incorrect_answers.add(answer)
                counter = len(self.incorrect_answers)
                print(f"sorry you got {counter} wrong!")

    def verifyAge(self,age):
        if age >= 18:
            print("access granted")
        else:
            print("access denied")
            


    def main(self):
        # user_age = float(input("input your age here:"))
        # verifyAge(user_age)
        self.answer_questions()
class QuizBrain:
    def __init__ (self, ques_list):
        self.question_number = 0
        self.ques_list = ques_list
        self.score = 0
    def still_has_question(self):
        if self.question_number == len(self.ques_list):
            return False
        else:
            return True

    def next_question(self):
        self.question_number += 1
        ans = str(input(f"Q. {self.question_number} , {self.ques_list[self.question_number - 1].question} " ))
        self.check_answer(ans , self.ques_list[self.question_number - 1].answer)

    def check_answer(self , answer , correct_answer):
        if answer == correct_answer:
            self.score += 1
            print(f'Correct, your current score is {self.score}.')
        elif answer != correct_answer:
            print(f'Incorrect, your current score is {self.score}.')
        else:
            print('Ye message nai dikhna chahiye')
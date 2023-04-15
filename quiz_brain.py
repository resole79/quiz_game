class QuizBrain:
    """Class QuizBrain
    # Instance
    question_list, question_number, score
    Method:
    still_has_question, check_answer, nex_question
    """
    def __init__(self, question_list):
        # instance
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    # Method to check if is still question left
    def still_has_question(self):
        """
        Method to check if are still question left
        return:
        has_question -> bool
        """
        has_question = False
        len_question = len(self.question_list)
        if self.question_number < len_question:
            has_question = True

        return has_question

    # Method to check if the answer are correct
    def check_answer(self, user_answ, correct_answer):
        """
        Method to check if the answer are correct
        accept:
        user_answ -> bool ( True / False )
        correct_answer -> bool ( True / False )
        """
        if user_answ.lower() == correct_answer.lower():
            print("Your answer has correct\n")
            self.score += 1
        else:
            print("Sorry your answer is not correct")
            print(f"The correct answer was {correct_answer}\n")

    # Method to show next question
    def nex_question(self):
        """
        Method to show next question
        """
        question_current = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question number {self.question_number} : {question_current.text} (True/False?): ")
        self.check_answer(user_answer, question_current.answer)

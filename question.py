class Question:
    def __init__(self, questionText, correctAnswer, incorrectAnswers):
        self.questionText = questionText
        self.correctAnswer = correctAnswer
        self.incorrectAnswers = incorrectAnswers
        self.allAnswers = [correctAnswer] + incorrectAnswers

    
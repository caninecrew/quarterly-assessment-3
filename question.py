import random
class Question:
    def __init__(self, questionText, correctAnswer, incorrectAnswers):
        self.questionText = questionText
        self.correctAnswer = correctAnswer
        self.incorrectAnswers = incorrectAnswers
        self.allAnswers = [correctAnswer] + incorrectAnswers
    
    def isCorrect(self, answer):
        return answer == self.correctAnswer
    
    def getShuffledAnswers(self):
        shuffled = self.allAnswers.copy()
        random.shuffle(shuffled)
        return shuffled
    

    
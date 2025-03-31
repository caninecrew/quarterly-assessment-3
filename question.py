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
    
    def display(self):
        print(f"Question: {self.questionText}")
        print("Answers:")
        for i, answer in enumerate(self.getShuffledAnswers(), start=1):
            print(f"{i}. {answer}")
            
    def __str__(self):
        return f"Question: {self.questionText}\nCorrect Answer: {self.correctAnswer}\nIncorrect Answers: {self.incorrectAnswers}"
    

    
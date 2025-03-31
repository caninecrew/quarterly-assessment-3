# format: question : [correct answer, incorrect answer, incorrect answer, incorrect answer],
questions = {
            "What is the capital of Spain?" : ["Madrid", "Barcelona", "Valencia", "Seville"],
            "Who was the second Vice President of the United States?" : ["Thomas Jefferson", "John Adams", "Aaron Burr", "George Clinton"],
            "What was the name of the son of Adam and Eve who killed his brother?" : ["Cain", "Abel", "Seth", "Noah"],
            "What does the TV network abbreviation CBS stand for?" : ["Columbia Broadcasting System", "Community Broadcasting Station", "Cable Broadcasting System", "Creative Broadcast Studios"],
            "How many of Henry VIII's wives were executed?" : ["two", "one", "three", "four"],
            "What is the name of the Mayflower's sister ship?" : ["Speedwell", "Camellia", "Lilac", "Sweetbriar"],
            "Where is the world's largest McDonald's located?" : ["Orlando, Flordia", "Paris, France", "London, England", "New York City, New York"],
}

class Question:
    def __init__(self, questionText, correctAnswer, incorrectAnswers):
        self.questionText = questionText
        self.correctAnswer = correctAnswer
        self.incorrectAnswers = incorrectAnswers
        self.allAnswers = [correctAnswer] + incorrectAnswers

    
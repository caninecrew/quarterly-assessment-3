import tkinter as tk
from tkinter import ttk, messagebox
from question import Question
from database import Database
import random as rand

class QuizInterface: # QuizInterface class for handling quiz operations
    def __init__(self, root=None):  
        self.db = Database()
        self.questions = []
        self.currentQuestionIndex = 0
        self.score = 0
        self.category = None
        self.root = root

    def getQuestionsFromCategory(self, category, numQuestions=5):
        """Fetch questions from the specified category"""
        self.category = category
        questionDicts = self.db.getRandomQuestions(category, numQuestions)
        
        # Convert dictionaries to Question objects
        self.questions = []
        for q_dict in questionDicts:
            question = Question(
                q_dict["question"],
                q_dict["correctAnswer"],
                q_dict["incorrectAnswers"]
            )
            # Add category and ID as attributes
            question.category = category
            question.id = q_dict["id"]
            self.questions.append(question)
        
        self.currentQuestionIndex = 0
        self.score = 0
        return len(self.questions) > 0
    
    def getCurrentQuestion(self):
        """Return the current question object"""
        if 0 <= self.currentQuestionIndex < len(self.questions):
            return self.questions[self.currentQuestionIndex]
        return None
    
    def checkAnswer(self, selectedAnswer):
        """Check if the selected answer is correct"""
        currentQuestion = self.getCurrentQuestion()
        if currentQuestion and currentQuestion.isCorrect(selectedAnswer):
            self.score += 1
            return True
        return False
    
    def nextQuestion(self):
        """Move to the next question"""
        self.currentQuestionIndex += 1
        return self.currentQuestionIndex < len(self.questions)

    def runTextInterface(self):
        """Run a text-based version of the quiz using Question objects"""
        print("Welcome to Quiz Bowl!")
        print("You will be asked 5 questions. Choose the correct answer from the options provided.")

        # Get available categories
        categories = self.db.getCategories()
        print("Available categories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        # Get user category choice
        while True:
            try:
                choice = int(input("Select a category (enter number): "))
                if 1 <= choice <= len(categories):
                    selected_category = categories[choice-1]
                    break
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

        # Get questions from selected category
        if not self.getQuestionsFromCategory(selected_category, 5):
            print("No questions available in this category.")
            return

        print(f"\nStarting quiz in {selected_category} category!")
        print(f"You will answer {len(self.questions)} questions.\n")

        for i in range(len(self.questions)): 
            currentQuestion = self.getCurrentQuestion()
            
            if not currentQuestion:
                break

            print(f"Question {i+1}/{len(self.questions)}:")
            print(currentQuestion.questionText) # print the question text

            # Get shuffled answers and display with letter options
            answers = currentQuestion.getShuffledAnswers() # get shuffled answers
            options = "abcd" # letter options

            for j, answer in enumerate(answers):
                if j < len(options):
                    print(f"{options[j]}) {answer}")

            pick = input("Choose a, b, c, or d: ").lower() # user selection

            while pick not in options[:len(answers)]:
                pick = input("You must choose either a, b, c, or d: ").lower()

            answerIndex = options.index(pick)
            selectedAnswer = answers[answerIndex] # get the selected answer

            if self.checkAnswer(selectedAnswer): # check if the answer is correct
                print("You have chosen correctly")
            else:  
                print(f"You have chosen incorrectly. The correct answer was: {currentQuestion.correctAnswer}")
            
            # Move to the next question
            self.nextQuestion()

        # Display Final Score after all questions
        print(f"\nThank you for playing! You answered {self.score} questions correctly.")
        print(f"Score: {self.score}/{len(self.questions)}")
        input("Press 'Enter' to EXIT")


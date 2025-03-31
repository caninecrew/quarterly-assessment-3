import tkinter as tk
from tkinter import ttk, messagebox, font
from quizInterface import QuizInterface

class QuizUI:
    def __init__(self, root, category, parentWindow):
        """Initialize the Quiz UI with the given root window, category, and parent window"""
        self.root = root
        self.category = category
        self.parentWindow = parentWindow
        self.quizInterface = QuizInterface(root)
        
        # Configure the root window
        self.root.title(f"Quiz Bowl - {category}")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        
        # Check if we can get questions
        success = self.quizInterface.getQuestionsFromCategory(category, 5)
        
        if not success:
            messagebox.showerror("Error", f"No questions available in {category} category")
            self.on_exit()
            return
        
        # Set up the UI components
        self.setupUI()
        
        # Start with the first question
        self.displayCurrentQuestion()
    
    def setupUI(self):
        """Set up the user interface components"""
        # Create styles
        style = ttk.Style()
        style.configure('Quiz.TFrame', background='#f0f0f0')
        style.configure('Quiz.TLabel', background='#f0f0f0', font=('Arial', 14))
        style.configure('Quiz.TButton', font=('Arial', 12))
        
        # Main content frame - will hold questions and answers
        self.contentFrame = ttk.Frame(self.root, style='Quiz.TFrame', padding=20)
        self.contentFrame.pack(expand=True, fill="both")
        
        # Question header - shows question number
        self.questionCounter = ttk.Label(
            self.contentFrame, 
            text="Question 1/5", 
            style='Quiz.TLabel',
            font=('Arial', 12, 'bold')
        )
        self.questionCounter.pack(pady=(0, 10))
        
        # Question text display
        self.questionLabel = ttk.Label(
            self.contentFrame,
            text="",
            style='Quiz.TLabel',
            wraplength=700
        )
        self.questionLabel.pack(pady=20)
        
        # Frame for answer buttons
        self.answersFrame = ttk.Frame(self.contentFrame, style='Quiz.TFrame')
        self.answersFrame.pack(pady=20, fill="x")
        
        # Create answer buttons
        self.answerButtons = []
        for i in range(4):  # Assuming 4 answers (1 correct + 3 incorrect)
            btn = ttk.Button(
                self.answersFrame,
                text="",
                style='Quiz.TButton'
            )
            btn.pack(pady=5, fill="x")
            self.answerButtons.append(btn)
        
        # Feedback label - shows if answer was right or wrong
        self.feedbackLabel = ttk.Label(
            self.contentFrame,
            text="",
            style='Quiz.TLabel',
            font=('Arial', 12, 'italic')
        )
        self.feedbackLabel.pack(pady=10)
        
        # Score display
        self.scoreLabel = ttk.Label(
            self.contentFrame,
            text="Score: 0/0",
            style='Quiz.TLabel'
        )
        self.scoreLabel.pack(pady=10)
        
        # Next button - enabled after answering
        self.nextButton = ttk.Button(
            self.contentFrame,
            text="Next Question",
            command=self.nextQuestion,
            state="disabled"
        )
        self.nextButton.pack(pady=10)
        
        # Navigation frame at bottom
        self.navFrame = ttk.Frame(self.root, style='Quiz.TFrame')
        self.navFrame.pack(side="bottom", fill="x", pady=10, padx=20)
        
        # Back button to return to categories
        self.backButton = ttk.Button(
            self.navFrame,
            text="Back to Categories",
            command=self.on_exit
        )
        self.backButton.pack(side="right")

    def displayCurrentQuestion(self):
        """Display the current question and answers"""
        currentQuestion = self.quizInterface.getCurrentQuestion()
        
        if not currentQuestion:
            self.showQuizResults()
            return
        
        # Update question counter
        questionNum = self.quizInterface.currentQuestionIndex + 1
        totalQuestions = len(self.quizInterface.questions)
        self.questionCounter.config(text=f"Question {questionNum}/{totalQuestions}")
        
        # Update question text
        self.questionLabel.config(text=currentQuestion.questionText)
        
        # Get shuffled answers
        answers = currentQuestion.getShuffledAnswers()
        
        # Reset feedback and next button
        self.feedbackLabel.config(text="")
        self.nextButton.config(state="disabled")
        
        # Update answer buttons
        for i, button in enumerate(self.answerButtons):
            if i < len(answers):
                answer = answers[i]
                button.config(
                    text=answer,
                    command=lambda ans=answer: self.checkAnswer(ans),
                    state="normal"
                )
            else:
                button.config(text="", state="disabled")
        
        # Update score display
        self.scoreLabel.config(
            text=f"Score: {self.quizInterface.score}/{totalQuestions}"
        )

    def checkAnswer(self, selectedAnswer):
        """Check if the selected answer is correct"""
        # Disable all answer buttons after selection
        for button in self.answerButtons:
            button.config(state="disabled")
        
        # Check the answer
        isCorrect = self.quizInterface.checkAnswer(selectedAnswer)
        
        # Show feedback
        if isCorrect:
            self.feedbackLabel.config(
                text="Correct! Well done.",
                foreground="green"
            )
        else:
            correctAnswer = self.quizInterface.getCurrentQuestion().correctAnswer
            self.feedbackLabel.config(
                text=f"Incorrect. The correct answer is: {correctAnswer}",
                foreground="red"
            )
        
        # Update score
        totalQuestions = len(self.quizInterface.questions)
        self.scoreLabel.config(
            text=f"Score: {self.quizInterface.score}/{totalQuestions}"
        )
        
        # Enable next button
        self.nextButton.config(state="normal")

    def nextQuestion(self):
        """Move to the next question"""
        hasMore = self.quizInterface.nextQuestion()
        
        if hasMore:
            self.displayCurrentQuestion()
        else:
            self.showQuizResults()

    def showQuizResults(self):
        """Show the final quiz results"""
        # Clear the content frame
        for widget in self.contentFrame.winfo_children():
            widget.destroy()
        
        # Create result title
        resultsTitle = ttk.Label(
            self.contentFrame,
            text="Quiz Complete!",
            font=('Arial', 24, 'bold'),
            style='Quiz.TLabel'
        )
        resultsTitle.pack(pady=20)
        
        # Show final score
        totalQuestions = len(self.quizInterface.questions)
        finalScore = self.quizInterface.score
        scoreDisplay = ttk.Label(
            self.contentFrame,
            text=f"Your Final Score: {finalScore}/{totalQuestions}",
            font=('Arial', 18),
            style='Quiz.TLabel'
        )
        scoreDisplay.pack(pady=10)
        
        # Calculate percentage
        percentage = (finalScore / totalQuestions) * 100
        
        # Show feedback message based on score
        if percentage >= 90:
            message = "Excellent! Outstanding performance!"
            color = "green"
        elif percentage >= 70:
            message = "Great job! You know this subject well!"
            color = "green"
        elif percentage >= 50:
            message = "Good effort! Keep studying to improve."
            color = "blue"
        else:
            message = "Keep practicing to improve your knowledge."
            color = "orange"
        
        feedbackMsg = ttk.Label(
            self.contentFrame,
            text=message,
            font=('Arial', 14, 'italic'),
            foreground=color
        )
        feedbackMsg.pack(pady=20)
        
        # Button frame for options
        buttonFrame = ttk.Frame(self.contentFrame, style='Quiz.TFrame')
        buttonFrame.pack(pady=20)
        
        # Try Again button
        tryAgainBtn = ttk.Button(
            buttonFrame,
            text="Try Again",
            command=self.restartQuiz,
            style='Quiz.TButton',
            width=15
        )
        tryAgainBtn.pack(side="left", padx=10)
        
        # Back to categories button
        backBtn = ttk.Button(
            buttonFrame,
            text="Back to Categories",
            command=self.on_exit,
            style='Quiz.TButton',
            width=15
        )
        backBtn.pack(side="left", padx=10)

    def restartQuiz(self):
        """Restart the current quiz"""
        # Get fresh questions from the same category
        success = self.quizInterface.getQuestionsFromCategory(self.category, 5)
        
        if not success:
            messagebox.showerror("Error", "Could not retrieve new questions. Please try again later.")
            return
        
        # Clear the content frame
        for widget in self.contentFrame.winfo_children():
            widget.destroy()
        
        # Set up the UI again
        self.setupUI()
        
        # Start with the first question
        self.displayCurrentQuestion()
    
    def on_exit(self):
        """Handle exiting the quiz"""
        self.root.destroy()
        if self.parentWindow:
            self.parentWindow.deiconify()
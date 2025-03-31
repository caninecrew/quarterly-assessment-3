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
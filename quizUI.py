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
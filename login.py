import tkinter as tk
from tkinter import ttk, messagebox, font
from database import Database
from quizInterface import QuizInterface
from admin import *

class LoginScreen:
    def __init__(self):
        self.root = tk.Tk() # Initialize the root window
        self.root.title("Quiz Bowl Login")
        self.root.geometry("600X400")
        self.root.configure(bg="#f0f0f0")
        self.setupUI() # Setup the UI components
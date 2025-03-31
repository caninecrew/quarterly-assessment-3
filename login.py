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

    def setupUI(self):
        """Set up the user interface components"""
        # Configure styles
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12), padding=10)
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill="both")
        
        # Title
        title_font = font.Font(family='Arial', size=24, weight='bold')
        title = ttk.Label(main_frame, text="Welcome to Quiz Bowl", font=title_font)
        title.pack(pady=20)
        
        # Description
        description = ttk.Label(main_frame, text="Please select your role to continue:", font=('Arial', 14))
        description.pack(pady=10)
        
        # Buttons frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        # Quiz taker button
        quiz_btn = ttk.Button(btn_frame, text="Quiz Taker", 
                             command=self.open_quiz_taker)
        quiz_btn.pack(side="left", padx=10, pady=10, ipadx=20)
        
        # Admin button
        admin_btn = ttk.Button(btn_frame, text="Administrator", 
                              command=self.open_admin_login)
        admin_btn.pack(side="left", padx=10, pady=10, ipadx=20)
        
        # Exit button
        exit_btn = ttk.Button(main_frame, text="Exit", 
                             command=self.root.destroy)
        
        exit_btn.pack(pady=20)

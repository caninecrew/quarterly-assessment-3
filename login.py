import tkinter as tk
from tkinter import ttk, messagebox, font
from database import Database
from quizInterface import QuizInterface
from admin import *

class LoginScreen:
    def __init__(self):
        self.root = tk.Tk() # Initialize the root window
        self.root.title("Quiz Bowl Login")
        self.root.geometry("600x400")
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
        mainFrame = ttk.Frame(self.root, padding="20")
        mainFrame.pack(expand=True, fill="both")
        
        # Title
        titleFont = font.Font(family='Arial', size=24, weight='bold')
        title = ttk.Label(mainFrame, text="Welcome to Quiz Bowl", font=titleFont)
        title.pack(pady=20)
        
        # Description
        description = ttk.Label(mainFrame, text="Please select your role to continue:", font=('Arial', 14))
        description.pack(pady=10)
        
        # Buttons frame
        btnFrame = ttk.Frame(mainFrame)
        btnFrame.pack(pady=20)
        
        # Quiz taker button
        quizBtn = ttk.Button(btnFrame, text="Quiz Taker", 
                             command=self.openQuizTaker)
        quizBtn.pack(side="left", padx=10, pady=10, ipadx=20)
        
        # Admin button
        adminBtn = ttk.Button(btnFrame, text="Administrator", 
                              command=self.openAdminLogin)
        adminBtn.pack(side="left", padx=10, pady=10, ipadx=20)
        
        # Exit button
        exitBtn = ttk.Button(mainFrame, text="Exit", 
                             command=self.root.destroy)
        
        exitBtn.pack(pady=20)

loginScrn = LoginScreen()
loginScrn.root.mainloop() # Start the Tkinter main loop
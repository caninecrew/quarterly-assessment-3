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

    def openQuizTaker(self):
            """Opens the quiz taker interface"""
            # Hide the main window
            self.root.withdraw()
            
            # Create a new window for category selection
            categoryWindow = tk.Toplevel()
            categoryWindow.title("Quiz Bowl - Select Category")
            categoryWindow.geometry("600x400")
            categoryWindow.configure(bg="#f0f0f0")
            
            # Add a protocol to handle window closing
            categoryWindow.protocol("WM_DELETE_WINDOW", 
                                lambda: self.onClosing(categoryWindow))
            
            # Create the main frame
            mainFrame = ttk.Frame(categoryWindow, padding="20")
            mainFrame.pack(expand=True, fill="both")
            
            # Add title
            titleFont = font.Font(family='Arial', size=18, weight='bold')
            title = ttk.Label(mainFrame, text="Select a Quiz Category", font=titleFont)
            title.pack(pady=20)
            
            # Get categories from database
            db = Database()
            categories = db.getCategories()
            
            # Display categories as buttons
            for category in categories:
                # Format display name (e.g., "ComputerScience" -> "Computer Science")
                displayName = category
                if category == "ComputerScience":
                    displayName = "Computer Science"
                    
                btn = ttk.Button(mainFrame, text=displayName,
                            command=lambda cat=category: self.startQuiz(categoryWindow, cat))
                btn.pack(pady=5, fill="x")
            
            # Add back button
            backBtn = ttk.Button(mainFrame, text="Back to Login", 
                                command=lambda: self.goBackToLogin(categoryWindow))
            backBtn.pack(pady=20)

            
loginScrn = LoginScreen()
loginScrn.root.mainloop() # Start the Tkinter main loop
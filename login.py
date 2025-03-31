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

    def startQuiz(self, parentWindow, category):
        """Start the quiz with the selected category"""
        parentWindow.withdraw()
        
        # Create quiz window
        quizWindow = tk.Toplevel()
        quizWindow.title(f"Quiz Bowl - {category}")
        quizWindow.geometry("800x600")
        quizWindow.configure(bg="#f0f0f0")
        
        # Add protocol for window closing
        quizWindow.protocol("WM_DELETE_WINDOW", 
                        lambda: self.onClosing(quizWindow, parentWindow))
        
        # Create the QuizUI
        from quizUI import QuizUI
        quiz_ui = QuizUI(quizWindow, category, parentWindow)
        
    def openAdminLogin(self):
        """Opens the administrator login interface"""
        # Hide the main window
        self.root.withdraw()
        
        # Create admin login window
        adminWindow = tk.Toplevel()
        adminWindow.title("Quiz Bowl - Administrator Login")
        adminWindow.geometry("500x300")
        adminWindow.configure(bg="#f0f0f0")
        
        # Add a protocol to handle window closing
        adminWindow.protocol("WM_DELETE_WINDOW", 
                           lambda: self.onClosing(adminWindow))
        
        # Create the main frame
        mainFrame = ttk.Frame(adminWindow, padding="20")
        mainFrame.pack(expand=True, fill="both")
        
        # Add title
        titleFont = font.Font(family='Arial', size=18, weight='bold')
        title = ttk.Label(mainFrame, text="Administrator Login", font=titleFont)
        title.pack(pady=20)
        
        # Username field
        usernameFrame = ttk.Frame(mainFrame)
        usernameFrame.pack(fill="x", pady=5)
        
        usernameLabel = ttk.Label(usernameFrame, text="Username:")
        usernameLabel.pack(side="left", padx=5)
        
        usernameEntry = ttk.Entry(usernameFrame)
        usernameEntry.pack(side="left", expand=True, fill="x", padx=5)
        
        # Password field
        passwordFrame = ttk.Frame(mainFrame)
        passwordFrame.pack(fill="x", pady=5)
        
        passwordLabel = ttk.Label(passwordFrame, text="Password:")
        passwordLabel.pack(side="left", padx=5)
        
        passwordEntry = ttk.Entry(passwordFrame, show="*")
        passwordEntry.pack(side="left", expand=True, fill="x", padx=5)
        
        # Buttons frame
        btnFrame = ttk.Frame(mainFrame)
        btnFrame.pack(pady=20)
        
        # Login button
        loginBtn = ttk.Button(btnFrame, text="Login", 
                              command=lambda: self.verifyAdmin(
                                  usernameEntry.get(), 
                                  passwordEntry.get(), 
                                  adminWindow))
        loginBtn.pack(side="left", padx=5)
        
        # Back button
        backBtn = ttk.Button(btnFrame, text="Back", 
                             command=lambda: self.goBackToLogin(adminWindow))
        backBtn.pack(side="right", padx=5)
    
    def verifyAdmin(self, username, password, adminWindow):
        """Verify administrator credentials"""
        db = Database()
        if db.verifyAdminCredentials(username, password):
            messagebox.showinfo("Success", "Login successful!")
            adminWindow.destroy()
            # Here you would launch the admin interface
            # adminInterface = AdminInterface(self.root)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def goBackToLogin(self, currentWindow):
        """Return to the login screen"""
        currentWindow.destroy()
        self.root.deiconify()

    def goBackToCategory(self, quizWindow, categoryWindow):
        """Return to the category selection screen"""
        quizWindow.destroy()
        categoryWindow.deiconify()
    
    def onClosing(self, window, parentWindow=None):
        """Handle window closing"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
            if parentWindow:
                parentWindow.deiconify()
            else:
                self.root.deiconify()
    
    def run(self):
        """Run the main loop of the application"""
        self.root.mainloop()
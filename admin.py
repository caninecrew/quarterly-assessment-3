import tkinter as tk
from tkinter import ttk, messagebox, font
from database import Database

class AdminInterface:
    def __init__(self, root):
        self.root = root
        self.db = Database()

        # Create the main dashboard window
        self.adminWindow = tk.Toplevel(root)
        self.adminWindow.title("Quiz Bowl - Administrator Dashboard")
        self.adminWindow.geometry("900x600")
        self.adminWindow.configure(bg="#f0f0f0")
        
        # Protocol to handle window closing
        self.adminWindow.protocol("WM_DELETE_WINDOW", self.onExit)
        
        # Hide the parent window
        self.root.withdraw()
        
        # Setup the UI
        self.setupUI()

    def setupUI(self):
        # Configure style
        style = ttk.Style()
        style.configure('Admin.TFrame', background='#f0f0f0')
        style.configure('Admin.TLabel', background='#f0f0f0', font=('Arial', 12))
        style.configure('Admin.TButton', font=('Arial', 12), padding=10)
        
        # Main container
        mainFrame = ttk.Frame(self.adminWindow, style='Admin.TFrame', padding="20")
        mainFrame.pack(expand=True, fill="both")
        
        # Title
        titleFont = font.Font(family='Arial', size=24, weight='bold')
        title = ttk.Label(mainFrame, text="Administrator Dashboard", style='Admin.TLabel', font=titleFont)
        title.pack(pady=20)
        
        # Buttons for different admin functions
        buttonsFrame = ttk.Frame(mainFrame, style='Admin.TFrame')
        buttonsFrame.pack(pady=20)
        
        # Add Question button
        addBtn = ttk.Button(
            buttonsFrame, 
            text="Add New Question",
            command=self.openAddQuestion,
            style='Admin.TButton',
            width=25
        )
        addBtn.pack(pady=10)
        
        # View Questions button
        viewBtn = ttk.Button(
            buttonsFrame,
            text="View/Edit Questions",
            command=self.openViewQuestions,
            style='Admin.TButton',
            width=25
        )
        viewBtn.pack(pady=10)
        
        # Database Stats button
        statsBtn = ttk.Button(
            buttonsFrame,
            text="Database Statistics",
            command=self.showDatabaseStats,
            style='Admin.TButton',
            width=25
        )
        statsBtn.pack(pady=10)
        
        # Logout button
        logoutBtn = ttk.Button(
            mainFrame,
            text="Logout",
            command=self.onExit,
            style='Admin.TButton'
        )
        logoutBtn.pack(pady=20)

    def openAddQuestion(self):
        """Open the Add Question interface"""
        AddQuestion(self.adminWindow, self.db)
    
    def openViewQuestions(self):
        """Open the View/Edit Questions interface"""
        ViewQuestions(self.adminWindow, self.db)

    def showDatabaseStats(self):
        """Show database statistics"""
        # Get category counts
        categories = self.db.getCategories()
        stats = "Database Statistics:\n\n"
        
        total = 0
        for category in categories:
            count = self.db.questionCount(category)
            total += count
            stats += f"{category}: {count} questions\n"
        
        stats += f"\nTotal Questions: {total}"
        
        # Show in a message box
        messagebox.showinfo("Database Statistics", stats)

    def onExit(self):
        """Handle exiting the admin interface"""
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.adminWindow.destroy()
            self.root.deiconify()
    
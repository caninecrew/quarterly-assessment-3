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

class AddQuestion:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        
        # Create a new window
        self.window = tk.Toplevel(parent)
        self.window.title("Add New Question")
        self.window.geometry("700x600")
        self.window.configure(bg="#f0f0f0")
        
        # Setup the UI
        self.setupUI()
    
    def setupUI(self):
        # Main frame
        mainFrame = ttk.Frame(self.window, padding="20")
        mainFrame.pack(expand=True, fill="both")
        
        # Title
        title = ttk.Label(
            mainFrame, 
            text="Add New Question",
            font=('Arial', 18, 'bold')
        )
        title.pack(pady=10)
        
        # Form fields
        # Category selection
        categoryFrame = ttk.Frame(mainFrame)
        categoryFrame.pack(fill="x", pady=10)
        
        categoryLabel = ttk.Label(
            categoryFrame,
            text="Category:",
            width=15,
            anchor="e"
        )
        categoryLabel.pack(side="left", padx=5)
        
        self.categoryVar = tk.StringVar()
        categories = self.db.getCategories()
        categoryCombo = ttk.Combobox(
            categoryFrame,
            textvariable=self.categoryVar,
            values=categories,
            state="readonly",
            width=30
        )
        categoryCombo.pack(side="left", padx=5)
        if categories:
            categoryCombo.current(0)
        
        # Question text
        questionFrame = ttk.Frame(mainFrame)
        questionFrame.pack(fill="x", pady=10)
        
        questionLabel = ttk.Label(
            questionFrame,
            text="Question:",
            width=15,
            anchor="ne"
        )
        questionLabel.pack(side="left", padx=5)
        
        self.questionText = tk.Text(
            questionFrame,
            wrap="word",
            height=5,
            width=50
        )
        self.questionText.pack(side="left", padx=5)
        
        # Correct answer
        correctFrame = ttk.Frame(mainFrame)
        correctFrame.pack(fill="x", pady=10)
        
        correctLabel = ttk.Label(
            correctFrame,
            text="Correct Answer:",
            width=15,
            anchor="e"
        )
        correctLabel.pack(side="left", padx=5)
        
        self.correctAnswer = ttk.Entry(correctFrame, width=50)
        self.correctAnswer.pack(side="left", padx=5)
        
        # Incorrect answers
        incorrectFrames = []
        self.incorrectAnswers = []
        
        for i in range(3):
            frame = ttk.Frame(mainFrame)
            frame.pack(fill="x", pady=10)
            
            label = ttk.Label(
                frame,
                text=f"Incorrect Answer {i+1}:",
                width=15,
                anchor="e"
            )
            label.pack(side="left", padx=5)
            
            entry = ttk.Entry(frame, width=50)
            entry.pack(side="left", padx=5)
            
            incorrectFrames.append(frame)
            self.incorrectAnswers.append(entry)
        
        # Buttons
        buttonFrame = ttk.Frame(mainFrame)
        buttonFrame.pack(pady=20)
        
        saveBtn = ttk.Button(
            buttonFrame,
            text="Save Question",
            command=self.saveQuestion
        )
        saveBtn.pack(side="left", padx=10)
        
        cancelBtn = ttk.Button(
            buttonFrame,
            text="Cancel",
            command=self.window.destroy
        )
        cancelBtn.pack(side="left", padx=10)
    
    def saveQuestion(self):
        """Save the new question to the database"""
        # Get values from form
        category = self.categoryVar.get()
        questionText = self.questionText.get("1.0", "end-1c").strip()
        correct = self.correctAnswer.get().strip()
        incorrect = [entry.get().strip() for entry in self.incorrectAnswers]
        
        # Validate input
        if not category:
            messagebox.showerror("Error", "Please select a category")
            return
            
        if not questionText:
            messagebox.showerror("Error", "Please enter a question")
            return
            
        if not correct:
            messagebox.showerror("Error", "Please enter a correct answer")
            return
            
        # Check that all incorrect answers are provided
        if not all(incorrect):
            messagebox.showerror("Error", "Please enter all three incorrect answers")
            return
        
        # Add question to database
        success = self.db.addQuestion(category, questionText, correct, incorrect)
        
        if success:
            messagebox.showinfo("Success", "Question added successfully!")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Failed to add question. Please try again.")
    
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

class ViewQuestions:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        
        # Create a new window
        self.window = tk.Toplevel(parent)
        self.window.title("View/Edit Questions")
        self.window.geometry("900x700")
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
            text="View and Edit Questions",
            font=('Arial', 18, 'bold')
        )
        title.pack(pady=10)
        
        # Category filter
        filterFrame = ttk.Frame(mainFrame)
        filterFrame.pack(fill="x", pady=10)
        
        filterLabel = ttk.Label(
            filterFrame,
            text="Filter by Category:",
            width=15
        )
        filterLabel.pack(side="left", padx=5)
        
        self.categoryVar = tk.StringVar()
        categories = self.db.getCategories()
        categoryCombo = ttk.Combobox(
            filterFrame,
            textvariable=self.categoryVar,
            values=categories,
            state="readonly",
            width=30
        )
        categoryCombo.pack(side="left", padx=5)
        if categories:
            categoryCombo.current(0)
            
        loadBtn = ttk.Button(
            filterFrame,
            text="Load Questions",
            command=self.loadQuestions
        )
        loadBtn.pack(side="left", padx=20)
        
        # Search frame
        searchFrame = ttk.Frame(mainFrame)
        searchFrame.pack(fill="x", pady=10)
        
        searchLabel = ttk.Label(
            searchFrame,
            text="Search:",
            width=15
        )
        searchLabel.pack(side="left", padx=5)
        
        self.searchEntry = ttk.Entry(searchFrame, width=30)
        self.searchEntry.pack(side="left", padx=5)
        
        searchBtn = ttk.Button(
            searchFrame,
            text="Search",
            command=self.searchQuestions
        )
        searchBtn.pack(side="left", padx=5)
        
        # Questions list
        listFrame = ttk.Frame(mainFrame)
        listFrame.pack(fill="both", expand=True, pady=10)
        
        # Create treeview for questions
        self.tree = ttk.Treeview(
            listFrame, 
            columns=("ID", "Question", "Correct Answer"),
            show="headings"
        )
        
        # Configure columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Question", text="Question")
        self.tree.heading("Correct Answer", text="Correct Answer")
        
        self.tree.column("ID", width=50)
        self.tree.column("Question", width=500)
        self.tree.column("Correct Answer", width=200)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(listFrame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack the treeview and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind select event
        self.tree.bind("<<TreeviewSelect>>", self.onQuestionSelect)
        
        # Buttons for actions
        btnFrame = ttk.Frame(mainFrame)
        btnFrame.pack(fill="x", pady=10)
        
        self.editBtn = ttk.Button(
            btnFrame,
            text="Edit Selected",
            command=self.editQuestion,
            state="disabled"
        )
        self.editBtn.pack(side="left", padx=5)
        
        self.deleteBtn = ttk.Button(
            btnFrame,
            text="Delete Selected",
            command=self.deleteQuestion,
            state="disabled"
        )
        self.deleteBtn.pack(side="left", padx=5)
        
        closeBtn = ttk.Button(
            btnFrame,
            text="Close",
            command=self.window.destroy
        )
        closeBtn.pack(side="right", padx=5)
        
        # Load questions for the first category
        if categories:
            self.loadQuestions()
    
    def loadQuestions(self):
        """Load questions from the selected category"""
        category = self.categoryVar.get()
        if not category:
            messagebox.showerror("Error", "Please select a category")
            return
        
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get questions
        questions = self.db.getQuestions(category)
        
        # Add to treeview
        for q in questions:
            self.tree.insert("", "end", values=(q["id"], q["question"], q["correctAnswer"]))
    
    def searchQuestions(self):
        """Search for questions containing the search term"""
        searchTerm = self.searchEntry.get().strip()
        if not searchTerm:
            messagebox.showinfo("Info", "Please enter a search term")
            return
        
        category = self.categoryVar.get()
        if not category:
            messagebox.showerror("Error", "Please select a category")
            return
        
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get questions matching search
        questions = self.db.searchQuestions(category, searchTerm)
        
        # Add to treeview
        for q in questions:
            self.tree.insert("", "end", values=(q["id"], q["question"], q["correctAnswer"]))
        
        # Show message if no results
        if not questions:
            messagebox.showinfo("Search Results", f"No questions found matching '{searchTerm}'")
    
    def onQuestionSelect(self, event):
        """Enable buttons when a question is selected"""
        selected = self.tree.selection()
        
        if selected:
            self.editBtn.config(state="normal")
            self.deleteBtn.config(state="normal")
        else:
            self.editBtn.config(state="disabled")
            self.deleteBtn.config(state="disabled")
    
    def editQuestion(self):
        """Open edit interface for the selected question"""
        selected = self.tree.selection()
        
        if not selected:
            return
        
        # Get question ID and category
        item = self.tree.item(selected[0])
        questionId = item["values"][0]
        category = self.categoryVar.get()
        
        # Open edit dialog
        EditQuestion(self.window, self.db, category, questionId, self.loadQuestions)
    
    def deleteQuestion(self):
        """Delete the selected question"""
        selected = self.tree.selection()
        
        if not selected:
            return
        
        # Get question ID and category
        item = self.tree.item(selected[0])
        questionId = item["values"][0]
        questionText = item["values"][1]
        category = self.categoryVar.get()
        
        # Confirm deletion
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete this question?\n\n{questionText}"):
            success = self.db.deleteQuestion(category, questionId)
            
            if success:
                messagebox.showinfo("Success", "Question deleted successfully")
                self.loadQuestions()  # Reload questions
            else:
                messagebox.showerror("Error", "Failed to delete question")

class EditQuestion:
    def __init__(self, parent, db, category, questionId, reloadCallback):
        self.parent = parent
        self.db = db
        self.category = category
        self.questionId = questionId
        self.reloadCallback = reloadCallback
        
        # Create a new window
        self.window = tk.Toplevel(parent)
        self.window.title(f"Edit Question #{questionId}")
        self.window.geometry("700x600")
        self.window.configure(bg="#f0f0f0")
        
        # Load the question data
        self.loadQuestionData()
        
        # Setup the UI
        self.setupUI()
    
    def loadQuestionData(self):
        """Load question data from database"""
        conn = self.db.connect()
        if not conn:
            messagebox.showerror("Error", "Database connection failed")
            self.window.destroy()
            return
            
        cursor = conn.cursor()
        
        try:
            # Get the question data
            cursor.execute(f"SELECT * FROM {self.category} WHERE id = ?", (self.questionId,))
            questionData = cursor.fetchone()
            
            if not questionData:
                messagebox.showerror("Error", f"Question #{self.questionId} not found")
                self.window.destroy()
                conn.close()
                return
                
            # Store the data
            self.questionData = {
                "question": questionData[1],
                "correctAnswer": questionData[2],
                "incorrectAnswers": [
                    questionData[3],
                    questionData[4],
                    questionData[5]
                ]
            }
            
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
            self.window.destroy()
        finally:
            conn.close()
    
    def setupUI(self):
        # Main frame
        mainFrame = ttk.Frame(self.window, padding="20")
        mainFrame.pack(expand=True, fill="both")
        
        # Title
        title = ttk.Label(
            mainFrame, 
            text=f"Edit Question #{self.questionId}",
            font=('Arial', 18, 'bold')
        )
        title.pack(pady=10)
        
        # Category (not editable)
        categoryFrame = ttk.Frame(mainFrame)
        categoryFrame.pack(fill="x", pady=10)
        
        categoryLabel = ttk.Label(
            categoryFrame,
            text="Category:",
            width=15,
            anchor="e"
        )
        categoryLabel.pack(side="left", padx=5)
        
        categoryValue = ttk.Label(
            categoryFrame,
            text=self.category
        )
        categoryValue.pack(side="left", padx=5)
        
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
        self.questionText.insert("1.0", self.questionData["question"])
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
        self.correctAnswer.insert(0, self.questionData["correctAnswer"])
        self.correctAnswer.pack(side="left", padx=5)
        
        # Incorrect answers
        incorrectFrames = []
        self.incorrectAnswers = []
        
        for i in range(3):
            frame = ttk.Frame(mainFrame)
            frame.pack(fill="x", padyclass EditQuestion:
    def __init__(self, parent, db, category, questionId, reloadCallback):
        self.parent = parent
        self.db = db
        self.category = category
        self.questionId = questionId
        self.reloadCallback = reloadCallback
        
        # Create a new window
        self.window = tk.Toplevel(parent)
        self.window.title(f"Edit Question #{questionId}")
        self.window.geometry("700x600")
        self.window.configure(bg="#f0f0f0")
        
        # Load the question data
        self.loadQuestionData()
        
        # Setup the UI
        self.setupUI()
    
    def loadQuestionData(self):
        """Load question data from database"""
        conn = self.db.connect()
        if not conn:
            messagebox.showerror("Error", "Database connection failed")
            self.window.destroy()
            return
            
        cursor = conn.cursor()
        
        try:
            # Get the question data
            cursor.execute(f"SELECT * FROM {self.category} WHERE id = ?", (self.questionId,))
            questionData = cursor.fetchone()
            
            if not questionData:
                messagebox.showerror("Error", f"Question #{self.questionId} not found")
                self.window.destroy()
                conn.close()
                return
                
            # Store the data
            self.questionData = {
                "question": questionData[1],
                "correctAnswer": questionData[2],
                "incorrectAnswers": [
                    questionData[3],
                    questionData[4],
                    questionData[5]
                ]
            }
            
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
            self.window.destroy()
        finally:
            conn.close()
    
    def setupUI(self):
        # Main frame
        mainFrame = ttk.Frame(self.window, padding="20")
        mainFrame.pack(expand=True, fill="both")
        
        # Title
        title = ttk.Label(
            mainFrame, 
            text=f"Edit Question #{self.questionId}",
            font=('Arial', 18, 'bold')
        )
        title.pack(pady=10)
        
        # Category (not editable)
        categoryFrame = ttk.Frame(mainFrame)
        categoryFrame.pack(fill="x", pady=10)
        
        categoryLabel = ttk.Label(
            categoryFrame,
            text="Category:",
            width=15,
            anchor="e"
        )
        categoryLabel.pack(side="left", padx=5)
        
        categoryValue = ttk.Label(
            categoryFrame,
            text=self.category
        )
        categoryValue.pack(side="left", padx=5)
        
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
        self.questionText.insert("1.0", self.questionData["question"])
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
        self.correctAnswer.insert(0, self.questionData["correctAnswer"])
        self.correctAnswer.pack(side="left", padx=5)
        
        # Incorrect answers
        incorrectFrames = []
        self.incorrectAnswers = []
        
        for i in range(3):
            frame = ttk.Frame(mainFrame)
            frame.pack(fill="x", pady
    
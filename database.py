# Author: Samuel Rumbley
# Date: 3/31/2025
# Class: DS 3850-001
# Instructor: Dr. Grant Clary
# Assignment: Quarterly Assessment 3
# Description: Database operations for Quiz Bowl

import sqlite3

class Database:
    def __init__(self,dbFile="quizBowl.db"):
        self.dbFile = dbFile
        self.conn = None
        self.createTables()

    def _processQueryResults(self, cursor):
        """Process query results into a list of question dictionaries."""
        # This is an internal helper method
        questions = []
        for row in cursor.fetchall():
            questions.append({
                "id": row[0],
                "question": row[1],
                "correctAnswer": row[2],
                "incorrectAnswers": [row[3], row[4], row[5]]
            })
        return questions
    
    def _validateCategory(self, category):
        """Validate if the category exists in the database."""
        valid_categories = ["History", "Science", "Literature", "Mathematics", "ComputerScience"]
        if category not in valid_categories:
            print(f"Invalid category: {category}. Valid categories are: {', '.join(valid_categories)}")
            return False
        return True
    
    def beginSession(self):
        """Open a connection for multiple operations."""
        if self.conn is not None:
            print("Connection already established.")
            return True
        return self.createConnection()

    def endSession(self):
        """Close the connection after multiple operations."""
        self.closeConnection()
    
    def createConnection(self):
        """Create a database connection to the SQLite database specified by dbFile."""
        try:
            self.conn = sqlite3.connect(self.dbFile)
            print("Connection to database established.")
            return True
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return False
        
    def closeConnection(self):
        """Close the database connection. Returns True if successful, False otherwise."""

        if self.conn:
            self.conn.close()
            self.conn = None # Set the connection to None after closing it
            print("Connection to database closed.")
            return True
        else:
            print("No connection to close.")
            return False

    def createTables(self):
        """Create tables for all categories if they don't exist. Returns True if successful, False otherwise."""

        conn = self.createConnection() # Establish connection to the database
        # Create tables for course categories
        tables = [
            "History", "Science", "Literature", "Mathematics", "ComputerScience"
        ]

        try:
            cursor = conn.cursor()
            for table in tables:
                cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {table} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        question TEXT NOT NULL,
                        correctAnswer TEXT NOT NULL,
                        incorrectAnswer1 TEXT NOT NULL,
                        incorrectAnswer2 TEXT NOT NULL,
                        incorrectAnswer3 TEXT NOT NULL
                    )
                """)
            self.conn.commit()
            print("Tables created successfully.")
            return True
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            return False
        finally:
            self.closeConnection()

    def populateInitialQuestions(self):
        """Populate database with initial questions if tables are empty."""
        # Check if we need to add sample data
        if self.questionCount() > 0:
            print("Database already contains questions. Skipping initial population.")
            return True
            
        
        
        try:
            self.beginSession()
            for category, questions in sampleData.items():
                for q in questions:
                    self.addQuestion(
                        category,
                        q["question"],
                        q["correctAnswer"],
                        q["incorrectAnswers"]
                    )
            return True
        except Exception as e:
            print(f"Error populating initial questions: {e}")
            return False
        finally:
            self.endSession()


    def addQuestion(self, category, question, correctAnswer, incorrectAnswers):
        """Add a question to the database. Returns True if successful, False otherwise."""

        if not self._validateCategory(category):
            return False
        
        if len(incorrectAnswers) != 3:
            print("You must provide exactly 3 incorrect answers.")
            return False
        
        sessionExisted = self.conn is not None
        if not sessionExisted and not self.beginSession():
            return False
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"""
                INSERT INTO {category} (question, correctAnswer, incorrectAnswer1, incorrectAnswer2, incorrectAnswer3)
                VALUES (?, ?, ?, ?, ?)
            """, (question, correctAnswer, *incorrectAnswers))
            self.conn.commit()
            print("Question added successfully.")
            return True
        except sqlite3.Error as e:
            print(f"Error adding question: {e}")
            return False
        finally:
            if not sessionExisted: 
                self.endSession()

    def updateQuestion(self, category, questionId, question=None, correctAnswer=None, incorrectAnswers=None):
        """Update a question in the database. Returns True if successful, False otherwise."""

        if not self._validateCategory(category):
            return False
        
        if incorrectAnswers is not None and len(incorrectAnswers) != 3:
            print("You must provide exactly 3 incorrect answers.")
            return False
        
        sessionExisted = self.conn is not None
        if not sessionExisted and not self.beginSession():
            return False
        
        try:  
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {category} WHERE id = ?", (questionId,))
            row = cursor.fetchone()

            if not row:
                print(f"Question with ID {questionId} not found in {category}.")
                return False
            
            newQuestion = question if question is not None else row[1]
            newCorrectAnswer = correctAnswer if correctAnswer is not None else row[2]

            if incorrectAnswers is not None:
                newIncorrect1 = incorrectAnswers[0]
                newIncorrect2 = incorrectAnswers[1]
                newIncorrect3 = incorrectAnswers[2]
            else:
                newIncorrect1 = row[3]
                newIncorrect2 = row[4]
                newIncorrect3 = row[5]

            cursor.execute(f"""
                UPDATE {category}
                SET question = ?, correctAnswer = ?, incorrectAnswer1 = ?, incorrectAnswer2 = ?, incorrectAnswer3 = ?
                WHERE id = ?
            """, (newQuestion, newCorrectAnswer, newIncorrect1, newIncorrect2, newIncorrect3, questionId))

            self.conn.commit()

            if cursor.rowcount > 0:
                print(f"Question with ID {questionId} updated successfully.")
                return True
            else:
                print(f"No changes made to question with ID {questionId}.")
                return False
        except sqlite3.Error as e:
            print(f"Error updating question: {e}")
            return False
        finally:
            if not sessionExisted:  # Only close if we opened it
                self.endSession()

    def deleteQuestion(self, category, questionId):
        """Delete a question from the database. Returns True if successful, False otherwise."""

        if not self._validateCategory(category):
            return False
        
        sessionExisted = self.conn is not None
        if not sessionExisted and not self.beginSession():
            return False
        
        try:
            cursor = self.conn.cursor()

            # Check if the question exists before attempting to delete it
            cursor.execute(f"SELECT id FROM {category} WHERE id = ?", (questionId,))
            if not cursor.fetchone():
                print(f"Question with ID {questionId} not found in {category}.")
                return False

            # Delete the question from the database
            cursor.execute(f"DELETE FROM {category} WHERE id = ?", (questionId,)) 
            
            self.conn.commit()

            if cursor.rowcount > 0:
                print(f"Question with ID {questionId} deleted successfully.")
                return True
            else:
                print(f"No changes made to question with ID {questionId}.")
                return False
            
        except sqlite3.Error as e:
            print(f"Error deleting question: {e}")
            return False
        finally:
            if not sessionExisted:  # Only close if we opened it
                self.endSession()
        
    def getQuestions(self, category):
        """Retrieve all questions from the specified category. Returns a list of questions."""

        if not self._validateCategory(category):
            return []
        
        sessionExisted = self.conn is not None
        if not sessionExisted and not self.beginSession():
            return []
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {category}")  # Select all questions from the specified category table
            return self._processQueryResults(cursor)  # Use the helper method
        except sqlite3.Error as e:
            print(f"Error retrieving questions: {e}")
            return []
        finally:
            if not sessionExisted:  # Only close if we opened it
                self.endSession()

    def getRandomQuestions(self, category, limit=5):
        """Retrieve random questions from the specified category. Returns a list of questions."""

        if not self._validateCategory(category):
            return []  # Changed from False to [] for consistency with getQuestions
        
        sessionExisted = self.conn is not None
        if not sessionExisted and not self.beginSession():
            return []        
                
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {category} ORDER BY RANDOM() LIMIT ?", (limit,))  # Select random questions with a limit
            return self._processQueryResults(cursor)  # Use the helper method
        except sqlite3.Error as e:
            print(f"Error retrieving random questions: {e}")
            return []
        finally:
            if not sessionExisted:  # Only close if we opened it
                self.endSession()

    def questionCount(self, category=None):
        """Return the number of questions in a category or total across all categories."""
        
        sessionExisted = self.conn is not None
        if not sessionExisted and not self.beginSession():
            return 0
                
        try:
            cursor = self.conn.cursor()
            if category:
                if not self._validateCategory(category):  # Changed from _validate_category to _validateCategory for consistency
                    return 0
                cursor.execute(f"SELECT COUNT(*) FROM {category}")
                count = cursor.fetchone()[0]
            else:
                count = 0
                valid_categories = ["History", "Science", "Literature", "Mathematics", "ComputerScience"]
                for cat in valid_categories:  # Changed from get_all_categories() to use the existing list
                    cursor.execute(f"SELECT COUNT(*) FROM {cat}")
                    count += cursor.fetchone()[0]
            return count
        except sqlite3.Error as e:
            print(f"Error counting questions: {e}")
            return 0
        finally:
            if not sessionExisted:  # Only close if we opened it
                self.endSession()

    def searchQuestions(self, category, searchTerm):
        """Search for questions containing the search term."""
        if not self._validateCategory(category):
            return []
        
        sessionExisted = self.conn is not None
        if not sessionExisted and not self.beginSession():
            return []
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {category} WHERE question LIKE ?", (f'%{searchTerm}%',))
            return self._processQueryResults(cursor)
        except sqlite3.Error as e:
            print(f"Error searching questions: {e}")
            return []
        finally:
            if not sessionExisted:
                self.endSession()

    def getCategories(self):
        """Return a list of all categories in the database."""
        return ["History", "Science", "Literature", "Mathematics", "ComputerScience"]
    
    def verifyAdminCredentials(self, username, password):
        """Verify admin credentials."""
        
        ADMIN_USERNAME = "admin"
        ADMIN_PASSWORD = "password123" # Use a secure password in production

        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD






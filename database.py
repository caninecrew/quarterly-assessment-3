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
    
    def createConnection(self):
        try:
            self.conn = sqlite3.connect(self.dbFile)
            print("Connection to database established.")
            return self.conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None
        
    def closeConnection(self):
        if self.conn:
            self.conn.close()
            print("Connection to database closed.")
        else:
            print("No connection to close.")

    def createTables(self):
        
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
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
        finally:
            self.closeConnection()

    def addQuestion(self, category, question, correctAnswer, incorrectAnswers):
        if len(incorrectAnswers) != 3: # Ensure exactly 3 incorrect answers are provided
            print("You must provide exactly 3 incorrect answers.")
            return
        
        try:
            conn = self.createConnection() # Establish connection to the database
            if not conn: # Check if the connection was successful
                return []
            cursor = conn.cursor() # Create a cursor object to execute SQL commands
            cursor.execute(f"""
                INSERT INTO {category} (question, correctAnswer, incorrectAnswer1, incorrectAnswer2, incorrectAnswer3)
                VALUES (?, ?, ?, ?, ?)
            """, (question, correctAnswer, *incorrectAnswers)) # Unpack the list of incorrect answers
            conn.commit() # Commit the changes to the database
            print("Question added successfully.") # Insert the question into the specified category table
        except sqlite3.Error as e:
            print(f"Error adding question: {e}") # Handle any errors that occur during the insertion process
        finally:
            self.closeConnection()

    def updateQuestion(self, category, questionId, question=None, correctAnswer=None, incorrectAnswers=None):
        
        # Checkthat incorrectAnswers is a list of 3 items if provided
        if incorrectAnswers is not None and len(incorrectAnswers) != 3:
            print("You must provide exactly 3 incorrect answers.")
            return False
        
        conn = self.createConnection() # Establish connection to the database
        if not conn: # Check if the connection was successful
            return False
        
        try:
            cursor = conn.cursor()

            cursor.execute(f"SELECT * FROM {category} WHERE id = ?", (questionId,)) # Select the question by ID
            row = cursor.fetchone() # Fetch the question from the database

            if not row: # Check if the question exists
                print(f"Question with ID {questionId} not found in {category}.")
                return False
            
            # Use existing values if new ones aren't provided
            new_question = question if question is not None else row[1]
            new_correctAnswer = correctAnswer if correctAnswer is not None else row[2]

            if incorrectAnswers is not None: # Unpack the list of incorrect answers
                newIncorrect1 = incorrectAnswers[0]
                newIncorrect2 = incorrectAnswers[1]
                newIncorrect3 = incorrectAnswers[2]
            else: # Use existing values if new ones aren't provided
                newIncorrect1 = row[3]
                newIncorrect2 = row[4]
                newIncorrect3 = row[5]

            # Update the question in the database
            cursor.execute(f"""
                UPDATE {category}
                SET question = ?, correctAnswer = ?, incorrectAnswer1 = ?, incorrectAnswer2 = ?, incorrectAnswer3 = ?
                WHERE id = ?
            """, (new_question, new_correctAnswer, newIncorrect1, newIncorrect2, newIncorrect3, questionId))

            conn.commit() # Commit the changes to the database

            if cursor.rowcount > 0: # Check if any rows were updated
                print(f"Question with ID {questionId} updated successfully.")
                return True
            else:
                print(f"No changes made to question with ID {questionId}.")
                return False

        except sqlite3.Error as e: # Handle any errors that occur during the update process
            print(f"Error updating question: {e}")
            return False
        finally:
            self.closeConnection()
        
    def getQuestions(self, category):
        conn = self.createConnection()
        if not conn: # Check if the connection was successful
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {category}") # Select all questions from the specified category table

            questions = []
            for row in cursor.fetchall():
                questions.append({
                    "id": row[0],
                    "question": row[1],
                    "correctAnswer": row[2],
                    "incorrectAnswers": [row[3], row[4], row[5]]
                })
            return questions # Return the list of questions
        except sqlite3.Error as e:
            print(f"Error retrieving questions: {e}")
            return []
        finally:
            self.closeConnection()


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


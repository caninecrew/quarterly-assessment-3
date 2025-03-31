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
        # Create tables for course categories
        tables = [
            "History", "Science", "Literature", "Mathematics", "ComputerScience"
        ]
        
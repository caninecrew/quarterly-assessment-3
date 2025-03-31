from database import Database
from login import LoginScreen
import os

def main():
    """
    Main entry point for the Quiz Bowl application.
    Initializes the database and launches the login screen.
    """
    print("Starting Quiz Bowl application...")
    
    # Check database status
    db_file = "quizBowl.db"
    if os.path.exists(db_file):
        print(f"Database file {db_file} found")
    else:
        print(f"Database file {db_file} not found, will be created")
    
    # Initialize database
    print("Initializing database connection...")
    db = Database()
    
    # Check current question count
    total_questions = db.questionCount()
    print(f"Database contains {total_questions} questions before population")
    
    # Populate with initial questions if needed
    if total_questions == 0:
        print("Database is empty. Populating with sample questions...")
        success = db.populateInitialQuestions()
        print(f"Database population {'successful' if success else 'failed'}")
    else:
        print("Database already contains questions. Checking category counts...")
    
    # Print category statistics
    categories = db.getCategories()
    for category in categories:
        count = db.questionCount(category)
        print(f"  - {category}: {count} questions")
    
    # Launch the login screen
    print("Starting user interface...")
    app = LoginScreen()
    app.run()

if __name__ == "__main__":
    main()
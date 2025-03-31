from database import Database
from login import LoginScreen

def main():
    """
    Main entry point for the Quiz Bowl application.
    Initializes the database and launches the login screen.
    """
    # Initialize database and populate with sample questions if empty
    db = Database()
    db.populateInitialQuestions()
    
    # Launch the login screen
    app = LoginScreen()
    app.run()

if __name__ == "__main__":
    main()
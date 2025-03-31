# Quiz Bowl Application

A Python quiz application developed for DS3850 Quarterly Assessment 3. This application allows users to take quizzes in different categories and administrators to manage questions.

## Features

- **User Features:**
  - Select from 5 different quiz categories
  - Take interactive quizzes with multiple-choice questions
  - Receive immediate feedback on answers
  - View final score and performance summary

- **Administrator Features:**
  - Secure login system
  - Add new questions to any category
  - View, edit, and delete existing questions
  - Search questions by text
  - View database statistics and question counts

## Installation

1. Clone this repository
2. Ensure Python 3.7+ is installed
3. Install required packages: `pip install tk sqlite3`
4. Run the application: `python main.py`

## Usage

### As a Quiz Taker
1. Start the application and select "Take Quiz"
2. Choose a category
3. Answer the questions
4. View your final score

### As an Administrator
1. Start the application and select "Administrator"
2. Login with credentials:
   - Username: admin
   - Password: password123
3. Use the dashboard to manage questions

## Project Structure

- `main.py` - Application entry point
- `database.py` - Database management
- `login.py` - Authentication screens
- `admin.py` - Administrator interface
- `quiz.py` - Quiz interface
- `question.py` - Question class

### Database Management
- Database class with session management
- Question storage in category-specific tables
- Functions for CRUD operations (Create, Read, Update, Delete)

### User Interface
- Login screen with role selection
- Quiz interface with multiple-choice questions
- Admin dashboard for question management

### Quiz Logic
- Question class for encapsulating quiz questions
- Random question selection
- Score tracking and feedback

## Technologies Used

- Python 3.8
- Tkinter for GUI
- SQLite for database

## Screenshots

[Consider adding screenshots of the main interfaces]

## Author

[Your Name]

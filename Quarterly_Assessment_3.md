# Quarterly Assessment 3: Quiz Bowl Application

## Overview

In this quarterly assessment, you will develop a comprehensive Quiz Bowl application with a graphical user interface (GUI). This project combines database management with frontend development to create a complete application experience.

### Project Components
- **Administrator Interface**: A password-protected section for managing quiz content
- **User Interface**: An accessible platform for taking quizzes

The quiz content should be based on courses you are currently enrolled in.

## Technical Requirements

### Database Structure
- Create a database with **5 different tables** (one for each course category)
- Each course table must contain **at least 10 questions** with corresponding answers
- Question data must include:
  - Question text
  - Multiple-choice options
  - Correct answer

### Administrator Interface
- Implement a secure login screen with password protection
- Create GUI forms for:
  - Adding new questions to the database
  - Viewing existing questions with filtering options
  - Editing or deleting questions
- Include intuitive navigation between administrative functions

### User Interface
- Design a welcoming start screen with quiz category selection
- Develop an interactive quiz interface that:
  - Displays questions with multiple-choice options
  - Processes user selections and submissions
  - Provides immediate feedback on answers
  - Tracks and displays the user's score throughout the quiz

### Programming Requirements
- Implement a **Question class** to handle question display and answer validation
- Use proper error handling for all database operations
- Apply object-oriented design principles throughout the application
- Include appropriate comments and documentation in your code

## Application Workflow

### Entry Point
- Create a login screen offering two distinct paths:
  - Administrator access (password-protected)
  - Quiz taker access (no authentication required)

### Administrator Workflow
Implement forms for:
- **Adding Questions**: 
  - Category selection
  - Question text input
  - Answer options configuration
  - Correct answer designation
- **Viewing Questions**: 
  - Category-based filtering
  - Comprehensive display options
- **Managing Questions**:
  - Modifying existing questions
  - Deleting questions from the database

### Quiz Taker Workflow
- Welcome screen with clear category selection
- Quiz interface presenting questions (either one-by-one or all at once)
- Interactive answer submission with immediate feedback
- Final score calculation and display

## Submission Requirements

Your GitHub repository must include:
- All Python source code files
- Database with preloaded question data for your courses
- README file with detailed usage instructions
- Commit history showing project progression
- A copy of your class schedule showing your name and T-number

## Evaluation Criteria

Your project will be evaluated based on:
- Complete functionality of all required features
- User interface design and overall usability
- Database design and implementation quality
- Error handling and robustness against edge cases
- Compliance with all submission requirements

---

**Due Date**: 04/13/2025


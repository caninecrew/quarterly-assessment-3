DRAFT

quiz_bowl/
├── database/
│   └── quiz_db.sqlite         # SQLite database file
├── models/
│   ├── __init__.py
│   ├── question.py            # Question class
│   └── database.py            # Database operations
├── views/
│   ├── __init__.py
│   ├── login.py               # Entry point screen
│   ├── admin/
│   │   ├── __init__.py
│   │   ├── admin_dashboard.py
│   │   ├── add_question.py
│   │   ├── view_questions.py
│   │   └── edit_question.py
│   └── quiz/
│       ├── __init__.py
│       ├── welcome.py
│       ├── quiz_interface.py
│       └── results.py
└── main.py                    # Application entry point
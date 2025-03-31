DRAFT

quiz_bowl/
├── database/
│   └── quiz_db.sqlite         # SQLite database file
├── models/'
│   ├── question.py            # Question class
│   └── database.py            # Database operations
├── views/
│   ├── login.py               # Entry point screen
│   ├── admin/
│   │   ├── admin_dashboard.py
│   │   ├── add_question.py
│   │   ├── view_questions.py
│   │   └── edit_question.py
│   └── quiz/
│       ├── quiz_interface.py
└── main.py                    # Application entry point
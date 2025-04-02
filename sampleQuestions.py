# ["ACCT 2120 - Principles of Accounting II", "DS 3620 - Bus Anyltcs:Data Drv Dec Makng", "DS 3810 - Prog Logic & Analytic Thinking", "DS 3850 - Business Applications Develop", "DS 3860 - Business Database Mgmt"]

SAMPLE_QUESTIONS = {
    "ACCT2120": [
        {"question": "Which financial statement shows a company's financial position at a specific point in time?", 
         "correctAnswer": "Balance Sheet", 
         "incorrectAnswers": ["Income Statement", "Statement of Cash Flows", "Statement of Retained Earnings"]},
        
        {"question": "The accounting equation is:", 
         "correctAnswer": "Assets = Liabilities + Equity", 
         "incorrectAnswers": ["Assets = Liabilities - Equity", "Equity = Assets + Liabilities", "Revenue - Expenses = Equity"]},
        
        {"question": "Which of the following is NOT a current asset?", 
         "correctAnswer": "Equipment", 
         "incorrectAnswers": ["Cash", "Accounts Receivable", "Inventory"]},
        
        {"question": "FIFO stands for:", 
         "correctAnswer": "First In, First Out", 
         "incorrectAnswers": ["First In, Final Out", "Financial Input, Fiscal Output", "Fixed Income, Fixed Outlay"]},
        
        {"question": "Depreciation is an example of:", 
         "correctAnswer": "A non-cash expense", 
         "incorrectAnswers": ["A liability", "A current asset", "Revenue"]},
        
        {"question": "What accounting principle states that businesses should record expenses in the same period as the revenues they helped generate?", 
         "correctAnswer": "Matching principle", 
         "incorrectAnswers": ["Conservatism principle", "Consistency principle", "Going concern principle"]},
        
        {"question": "Which method of inventory valuation typically results in higher net income during inflation?", 
         "correctAnswer": "FIFO", 
         "incorrectAnswers": ["LIFO", "Weighted Average", "Specific Identification"]},
        
        {"question": "Unearned revenue is considered what type of account?", 
         "correctAnswer": "Liability", 
         "incorrectAnswers": ["Asset", "Revenue", "Expense"]},
        
        {"question": "What is the journal entry to record the purchase of equipment with cash?", 
         "correctAnswer": "Dr Equipment, Cr Cash", 
         "incorrectAnswers": ["Dr Cash, Cr Equipment", "Dr Equipment, Cr Accounts Payable", "Dr Expense, Cr Cash"]},
        
        {"question": "The ability of a company to pay its short-term obligations is called:", 
         "correctAnswer": "Liquidity", 
         "incorrectAnswers": ["Solvency", "Profitability", "Efficiency"]}
    ],
    "DS3620": [
        {"question": "What type of analysis examines historical data to identify patterns and predict future outcomes?", 
         "correctAnswer": "Predictive analytics", 
         "incorrectAnswers": ["Descriptive analytics", "Prescriptive analytics", "Diagnostic analytics"]},

        {"question": "Which visualization is best for showing the relationship between two numerical variables?", 
         "correctAnswer": "Scatter plot", 
         "incorrectAnswers": ["Pie chart", "Bar chart", "Histogram"]},

        {"question": "What statistical measure represents the middle value in a dataset?", 
         "correctAnswer": "Median", 
         "incorrectAnswers": ["Mode", "Mean", "Range"]},

        {"question": "Which of the following is NOT a common data quality issue?", 
         "correctAnswer": "Data normalization", 
         "incorrectAnswers": ["Missing values", "Duplicate records", "Inconsistent formatting"]},

        {"question": "What does KPI stand for in business analytics?", 
         "correctAnswer": "Key Performance Indicator", 
         "incorrectAnswers": ["Knowledge Process Integration", "Key Process Input", "Knowledge Performance Index"]},

        {"question": "Which of these is a measure of data dispersion?", 
         "correctAnswer": "Standard deviation", 
         "incorrectAnswers": ["Mean", "Median", "Mode"]},

        {"question": "What type of analysis focuses on why something happened?", 
         "correctAnswer": "Diagnostic analytics", 
         "incorrectAnswers": ["Descriptive analytics", "Predictive analytics", "Prescriptive analytics"]},

        {"question": "Which programming language is NOT commonly used in data analytics?", 
         "correctAnswer": "Cobol", 
         "incorrectAnswers": ["Python", "R", "SQL"]},

        {"question": "What does ETL stand for in data management?", 
         "correctAnswer": "Extract, Transform, Load", 
         "incorrectAnswers": ["Export, Transfer, Link", "Evaluate, Test, Launch", "Electronic Transaction Log"]},

        {"question": "Which technique helps identify unusual patterns that do not conform to expected behavior?", 
         "correctAnswer": "Anomaly detection", 
         "incorrectAnswers": ["Regression analysis", "Cluster analysis", "Factor analysis"]}
    ],
    "DS3810": [
        {"question": "What is the primary goal of programming logic?", 
         "correctAnswer": "To solve problems systematically", 
         "incorrectAnswers": ["To write complex code", "To memorize syntax", "To debug errors"]},

        {"question": "Which of the following is a key component of programming logic?", 
         "correctAnswer": "Control structures", 
         "incorrectAnswers": ["Data visualization", "Database indexing", "Network protocols"]},

        {"question": "What is the purpose of a flowchart in programming?", 
         "correctAnswer": "To visually represent the steps in a process", 
         "incorrectAnswers": ["To write code", "To debug errors", "To compile programs"}},

        {"question": "Which of the following is an example of a conditional statement?", 
         "correctAnswer": "if-else", 
         "incorrectAnswers": ["for loop", "function call", "variable declaration"]},

        {"question": "What is the primary purpose of pseudocode?", 
         "correctAnswer": "To outline a program's logic in plain language", 
         "incorrectAnswers": ["To execute code", "To debug errors", "To compile programs"]},

        {"question": "Which of the following is NOT a common data type in programming?", 
         "correctAnswer": "Document", 
         "incorrectAnswers": ["Integer", "String", "Boolean"]},

        {"question": "What is an algorithm?", 
         "correctAnswer": "A step-by-step procedure for solving a problem", 
         "incorrectAnswers": ["A programming language", "A type of software", "A debugging tool"]},

        {"question": "Which of the following is an example of a loop structure?", 
         "correctAnswer": "while", 
         "incorrectAnswers": ["if", "switch", "case"]},

        {"question": "What is the purpose of debugging in programming?", 
         "correctAnswer": "To identify and fix errors in code", 
         "incorrectAnswers": ["To write new code", "To optimize performance", "To compile programs"]},

        {"question": "Which of the following best describes 'critical thinking' in programming?", 
         "correctAnswer": "Analyzing problems and designing effective solutions", 
         "incorrectAnswers": ["Memorizing syntax", "Writing complex code", "Following instructions without question"]}
    ],
    "DS3850": [
        {"question": "Which of the following is a Python GUI toolkit used in this course?", 
         "correctAnswer": "Tkinter", 
         "incorrectAnswers": ["PyQt", "Kivy", "wxPython"]},

        {"question": "What is the purpose of the __init__ method in Python?", 
         "correctAnswer": "To initialize a new object's attributes", 
         "incorrectAnswers": ["To import libraries", "To end the program execution", "To connect to a database"]},

        {"question": "What does OOP stand for in software development?", 
         "correctAnswer": "Object-Oriented Programming", 
         "incorrectAnswers": ["Ordered Operation Procedures", "Optimal Output Processing", "Ongoing Object Protocol"]},

        {"question": "Which database engine is used in the Quiz Bowl application?", 
         "correctAnswer": "SQLite", 
         "incorrectAnswers": ["MySQL", "MongoDB", "Oracle"]},

        {"question": "What is an event-driven programming model primarily used for?", 
         "correctAnswer": "GUI applications", 
         "incorrectAnswers": ["Data analysis", "Web servers", "Database management"]},

        {"question": "Which method is called when a Tkinter button is clicked?", 
         "correctAnswer": "The command callback function", 
         "incorrectAnswers": ["__init__()", "mainloop()", "update()"]},

        {"question": "What is the purpose of exception handling in Python?", 
         "correctAnswer": "To gracefully handle runtime errors", 
         "incorrectAnswers": ["To make code run faster", "To create user interfaces", "To connect to databases"]},

        {"question": "Which of the following is NOT a benefit of using classes?", 
         "correctAnswer": "Reduced memory usage", 
         "incorrectAnswers": ["Code reusability", "Encapsulation", "Inheritance"]},

        {"question": "What does CRUD stand for in application development?", 
         "correctAnswer": "Create, Read, Update, Delete", 
         "incorrectAnswers": ["Copy, Review, Undo, Debug", "Create, Run, Update, Deploy", "Code, Run, Update, Document"]},

        {"question": "Which design pattern separates data representation from user interface?", 
         "correctAnswer": "MVC (Model-View-Controller)", 
         "incorrectAnswers": ["Singleton", "Observer", "Factory"]}
    ],
    "DS3860": [
        {"question": "Which SQL statement is used to retrieve data from a database?", 
         "correctAnswer": "SELECT", 
         "incorrectAnswers": ["INSERT", "UPDATE", "DELETE"]},

        {"question": "What does SQL stand for?", 
         "correctAnswer": "Structured Query Language", 
         "incorrectAnswers": ["Simple Question Language", "System Quality Logic", "Standard Query Lookup"]},

        {"question": "Which of the following is a primary key constraint?", 
         "correctAnswer": "Uniquely identifies each record in a table", 
         "incorrectAnswers": ["Can have duplicate values", "Can be null", "Multiple can exist in a table"]},

        {"question": "What type of relationship exists when one record in a table is related to many records in another table?", 
         "correctAnswer": "One-to-many", 
         "incorrectAnswers": ["Many-to-many", "One-to-one", "Self-referencing"]},

        {"question": "What does DBMS stand for?", 
         "correctAnswer": "Database Management System", 
         "incorrectAnswers": ["Data Building and Management Software", "Database Maintenance Service", "Digital Business Management System"]},

        {"question": "Which normal form eliminates transitive dependencies?", 
         "correctAnswer": "Third Normal Form (3NF)", 
         "incorrectAnswers": ["First Normal Form (1NF)", "Second Normal Form (2NF)", "Boyce-Codd Normal Form (BCNF)"]},

        {"question": "Which SQL join returns rows when there is at least one match in both tables?", 
         "correctAnswer": "INNER JOIN", 
         "incorrectAnswers": ["LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"]},

        {"question": "What is an entity in database design?", 
         "correctAnswer": "A person, place, object, event, or concept about which data is stored", 
         "incorrectAnswers": ["A column in a table", "A relationship between tables", "A constraint on data values"]},

        {"question": "What is the purpose of an index in a database?", 
         "correctAnswer": "To speed up data retrieval operations", 
         "incorrectAnswers": ["To enforce data integrity", "To create relationships between tables", "To store backup data"]},

        {"question": "Which statement is used to combine the results of two SELECT statements?", 
         "correctAnswer": "UNION", 
         "incorrectAnswers": ["JOIN", "MERGE", "COMBINE"]}
    ]
}


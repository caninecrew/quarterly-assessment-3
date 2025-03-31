# ["History", "Science", "Literature", "Mathematics", "ComputerScience"]

SAMPLE_QUESTIONS = {
    "History": [
        {"question": "Who was the U.S. President during the signing of the Civil Rights Act of 1964?", 
         "correctAnswer": "Lyndon B. Johnson", 
         "incorrectAnswers": ["Dwight D. Eisenhower", "John F. Kennedy", "Richard Nixon"]},
        
        {"question": "What year was the Boy Scouts of America officially founded?", 
         "correctAnswer": "1910", 
         "incorrectAnswers": ["1890", "1929", "1935"]},
        
        {"question": "The term 'Trail of Tears' refers to the forced relocation of which Native American tribe, among others?", 
         "correctAnswer": "Cherokee", 
         "incorrectAnswers": ["Sioux", "Apache", "Iroquois"]},
        
        {"question": "Who was the first Secretary of the Treasury and is featured on the $10 bill?", 
         "correctAnswer": "Alexander Hamilton", 
         "incorrectAnswers": ["Thomas Jefferson", "John Adams", "Andrew Jackson"]},
        
        {"question": "Which of the following conflicts occurred first?", 
         "correctAnswer": "Spanish-American War", 
         "incorrectAnswers": ["Vietnam War", "Korean War", "World War II"]},
        
        {"question": "What document begins with the phrase 'When in the course of human events...'", 
         "correctAnswer": "Declaration of Independence", 
         "incorrectAnswers": ["U.S. Constitution", "Federalist Papers", "Emancipation Proclamation"]},
        
        {"question": "Who led the March on Washington and gave the 'I Have a Dream' speech in 1963?", 
         "correctAnswer": "Martin Luther King Jr.", 
         "incorrectAnswers": ["Malcolm X", "Thurgood Marshall", "John Lewis"]},
        
        {"question": "What was the purpose of the Lewis and Clark Expedition?", 
         "correctAnswer": "To explore and map the Louisiana Territory", 
         "incorrectAnswers": ["To defeat Native tribes", "To build early railroads", "To find a route to Asia"]},
        
        {"question": "What year did the United States land astronauts on the moon for the first time?", 
         "correctAnswer": "1969", 
         "incorrectAnswers": ["1965", "1967", "1972"]},
        
        {"question": "Which U.S. President warned against the formation of political parties in his farewell address?", 
         "correctAnswer": "George Washington", 
         "incorrectAnswers": ["Abraham Lincoln", "James Madison", "Thomas Jefferson"]}
    ],
    "Science": [
        {"question": "Which gas is most commonly found in Earth's atmosphere?", 
         "correctAnswer": "Nitrogen", 
         "incorrectAnswers": ["Oxygen", "Carbon Dioxide", "Argon"]},

        {"question": "What is the process by which plants convert sunlight into energy?", 
         "correctAnswer": "Photosynthesis", 
         "incorrectAnswers": ["Respiration", "Fermentation", "Transpiration"]},

        {"question": "What kind of rock is formed by volcanic activity?", 
         "correctAnswer": "Igneous", 
         "incorrectAnswers": ["Sedimentary", "Metamorphic", "Fossil"]},

        {"question": "Which part of the compass always points north?", 
         "correctAnswer": "Magnetized needle", 
         "incorrectAnswers": ["Baseplate", "Dial", "Direction of travel arrow"]},

        {"question": "Which organ in the human body filters blood to produce urine?", 
         "correctAnswer": "Kidney", 
         "incorrectAnswers": ["Liver", "Bladder", "Pancreas"]},

        {"question": "What type of energy is stored in food and fuel?", 
         "correctAnswer": "Chemical energy", 
         "incorrectAnswers": ["Thermal energy", "Kinetic energy", "Nuclear energy"]},

        {"question": "Which constellation contains the North Star?", 
         "correctAnswer": "Ursa Minor", 
         "incorrectAnswers": ["Orion", "Ursa Major", "Cassiopeia"]},

        {"question": "What weather instrument is used to measure air pressure?", 
         "correctAnswer": "Barometer", 
         "incorrectAnswers": ["Hygrometer", "Anemometer", "Thermometer"]},

        {"question": "Which macronutrient is primarily responsible for building muscle?", 
         "correctAnswer": "Protein", 
         "incorrectAnswers": ["Carbohydrates", "Fats", "Vitamins"]},

        {"question": "What type of tree loses its leaves annually?", 
         "correctAnswer": "Deciduous", 
         "incorrectAnswers": ["Coniferous", "Evergreen", "Perennial"]}
    ],
    "Literature": [
        {"question": "Who wrote *To Kill a Mockingbird*, a novel that explores themes of justice and morality?", 
         "correctAnswer": "Harper Lee", 
         "incorrectAnswers": ["Mark Twain", "F. Scott Fitzgerald", "John Steinbeck"]},

        {"question": "What is the name of the boy who leads the group in *Lord of the Flies* before things fall apart?", 
         "correctAnswer": "Ralph", 
         "incorrectAnswers": ["Jack", "Simon", "Piggy"]},

        {"question": "*The Call of the Wild* is set in which harsh, rugged environment?", 
         "correctAnswer": "Yukon Territory", 
         "incorrectAnswers": ["Rocky Mountains", "Alaskan Coast", "Sierra Nevada"]},

        {"question": "Which American author is known for adventure novels such as *The Adventures of Tom Sawyer* and *Huckleberry Finn*?", 
         "correctAnswer": "Mark Twain", 
         "incorrectAnswers": ["Ernest Hemingway", "Jack London", "Nathaniel Hawthorne"]},

        {"question": "What genre best describes *Hatchet* by Gary Paulsen?", 
         "correctAnswer": "Survival fiction", 
         "incorrectAnswers": ["Science fiction", "Mystery", "Historical fiction"]},

        {"question": "In *Of Mice and Men*, what is Lennie's dream along with George?", 
         "correctAnswer": "To own a small farm", 
         "incorrectAnswers": ["To strike gold", "To run a store", "To write a novel"]},

        {"question": "What famous dystopian novel begins with the line, 'It was a bright cold day in April, and the clocks were striking thirteen'?", 
         "correctAnswer": "*1984*", 
         "incorrectAnswers": ["*Fahrenheit 451*", "*Brave New World*", "*The Giver*"]},

        {"question": "Which character famously says, 'The greatest thing you'll ever learn is just to love and be loved in return'?", 
         "correctAnswer": "Christian from *Moulin Rouge!*", 
         "incorrectAnswers": ["Jay Gatsby", "Atticus Finch", "Romeo"]},

        {"question": "Which novel follows Scout Finch as she grows up in the racially segregated South?", 
         "correctAnswer": "*To Kill a Mockingbird*", 
         "incorrectAnswers": ["*The Secret Life of Bees*", "*A Separate Peace*", "*Roll of Thunder, Hear My Cry*"]},

        {"question": "Who wrote *Where the Red Fern Grows*, a story about a boy and his hunting dogs?", 
         "correctAnswer": "Wilson Rawls", 
         "incorrectAnswers": ["Lois Lowry", "Gary Paulsen", "Jack London"]}
    ],
    "Mathematics": [
        {"question": "What is the area of a triangle with a base of 10 inches and a height of 6 inches?", 
         "correctAnswer": "30 square inches", 
         "incorrectAnswers": ["60 square inches", "16 square inches", "20 square inches"]},

        {"question": "You have 3 trail mix bags, each weighing 1.5 pounds. What’s the total weight?", 
         "correctAnswer": "4.5 pounds", 
         "incorrectAnswers": ["3.5 pounds", "6 pounds", "5 pounds"]},

        {"question": "What is the next number in the sequence: 2, 4, 8, 16, ___?", 
         "correctAnswer": "32", 
         "incorrectAnswers": ["20", "30", "24"]},

        {"question": "If you split a $120 budget evenly among 8 Scouts, how much does each receive?", 
         "correctAnswer": "$15", 
         "incorrectAnswers": ["$12", "$14", "$10"]},

        {"question": "What is the mean of these numbers: 4, 8, 6, 10, 2?", 
         "correctAnswer": "6", 
         "incorrectAnswers": ["5", "7", "8"]},

        {"question": "A tent has a rectangular base 6 ft by 8 ft. What is the perimeter of the base?", 
         "correctAnswer": "28 ft", 
         "incorrectAnswers": ["48 ft", "36 ft", "14 ft"]},

        {"question": "What is 25% of 80?", 
         "correctAnswer": "20", 
         "incorrectAnswers": ["15", "18", "25"]},

        {"question": "What is the probability of flipping heads on a fair coin?", 
         "correctAnswer": "1/2", 
         "incorrectAnswers": ["1/4", "1/3", "2/3"]},

        {"question": "How many degrees are in the sum of interior angles of a triangle?", 
         "correctAnswer": "180", 
         "incorrectAnswers": ["90", "270", "360"]},

        {"question": "You hike 3 miles in 1 hour. At this rate, how far can you hike in 4 hours?", 
         "correctAnswer": "12 miles", 
         "incorrectAnswers": ["10 miles", "9 miles", "8 miles"]}
    ],
    "Computer Science": [
        {"question": "What does 'CPU' stand for in computing?", 
         "correctAnswer": "Central Processing Unit", 
         "incorrectAnswers": ["Computer Performance Unit", "Central Power Utility", "Core Processing Unit"]},

        {"question": "In Python, what symbol is used to begin a comment?", 
         "correctAnswer": "#", 
         "incorrectAnswers": ["//", "/*", "<!--"]},

        {"question": "Which data structure uses the First In, First Out (FIFO) principle?", 
         "correctAnswer": "Queue", 
         "incorrectAnswers": ["Stack", "List", "Dictionary"]},

        {"question": "What is the primary language used for querying databases?", 
         "correctAnswer": "SQL", 
         "incorrectAnswers": ["Python", "HTML", "C++"]},

        {"question": "Which of the following is NOT a type of loop in most programming languages?", 
         "correctAnswer": "Switch loop", 
         "incorrectAnswers": ["For loop", "While loop", "Do-while loop"]},

        {"question": "What type of value does a Boolean variable hold?", 
         "correctAnswer": "True or False", 
         "incorrectAnswers": ["String", "Integer", "Float"]},

        {"question": "Which HTML tag is used to create a hyperlink?", 
         "correctAnswer": "<a>", 
         "incorrectAnswers": ["<link>", "<href>", "<url>"]},

        {"question": "What is the name of the error when a program runs but gives incorrect output?", 
         "correctAnswer": "Logic error", 
         "incorrectAnswers": ["Syntax error", "Runtime error", "Compile-time error"]},

        {"question": "Which file extension is commonly associated with Python files?", 
         "correctAnswer": ".py", 
         "incorrectAnswers": [".java", ".exe", ".sql"]},

        {"question": "In programming, what is a function?", 
         "correctAnswer": "A reusable block of code that performs a task", 
         "incorrectAnswers": ["A comment in the code", "A type of variable", "A loop structure"]}
    ]
}


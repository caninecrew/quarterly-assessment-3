# Author: Samuel Rumbley
# Date: 3/31/2025
# Class: DS 3850-001
# Instructor: Dr. Grant Clary
# Assignment: Quarterly Assessment 3
# Description: Database operations for Quiz Bowl

import random as rand # random module (as rand)

varCorrectAnswer = 0

# format: question : [correct answer, incorrect answer, incorrect answer, incorrect answer],
questions = {
            "What is the capital of Spain?" : ["Madrid", "Barcelona", "Valencia", "Seville"],
            "Who was the second Vice President of the United States?" : ["Thomas Jefferson", "John Adams", "Aaron Burr", "George Clinton"],
            "What was the name of the son of Adam and Eve who killed his brother?" : ["Cain", "Abel", "Seth", "Noah"],
            "What does the TV network abbreviation CBS stand for?" : ["Columbia Broadcasting System", "Community Broadcasting Station", "Cable Broadcasting System", "Creative Broadcast Studios"],
            "How many of Henry VIII's wives were executed?" : ["two", "one", "three", "four"],
            "What is the name of the Mayflower's sister ship?" : ["Speedwell", "Camellia", "Lilac", "Sweetbriar"],
            "Where is the world's largest McDonald's located?" : ["Orlando, Flordia", "Paris, France", "London, England", "New York City, New York"],
}

questionsList = list(questions.keys()) # creates a list of all the keys to the dictionary (questions)
questionsGame = [] # the questions chosen for the game (initialize variable)
for i in range(0, 5): # choose a question 5 times using range() and a for loop
    questionsGame.append(rand.choice(questionsList)) # randonly select a choice from the questionsList and append to the list of questions for use in the game
rand.shuffle(questionsGame) # shuffle the questionsGame list

for ask in questionsGame: # for each question in the list of questions randomly chosen for this game
    answers = questions[ask] # seperate the answers list
    correctAns = answers[0] # retain the correct answer before shuffling
    rand.shuffle(answers) # shuffle the answers for the question

    print(ask) # print the question
    print("a)", answers[0]) # print the answers
    print("b)", answers[1])
    print("c)", answers[2])
    print("d)", answers[3])

    pick = input("Choose a, b, c, or d: ").lower() # user selection

    while pick != "a" and pick != "b" and pick != "c" and pick != "d": # while the user input is not a, b, c, or d
        pick = input("You must choose either a, b, c, or d: ").lower() # user selection

    if pick == "a": # assigns picked to equal the value of the answer chosen (as stated in the original dictionary)
        picked = answers[0]
    elif pick == "b":
        picked = answers[1]
    elif pick == "c":
        picked = answers[2]
    elif pick == "d":
        picked = answers[3]

    if picked == correctAns: # compare answer picked to correct answer
        print("You have chosen correctly") # print if equal
        varCorrectAnswer += 1 # add one point to the score

    elif picked != correctAns:  # compare answer picked to correct answer
        print("You have chosen incorrectly") # print if not equal
    
    print() # add space

print(f"Thank you for playing! You answered {varCorrectAnswer} questions correctly.")
print(f"Score: {varCorrectAnswer}/5")
input("Press 'Enter' to EXIT")
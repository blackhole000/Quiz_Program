# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed


quiz = {
    "Question1": {
        "Question": "What is the capital Turkey?",
        "Answer": "Ankara"
    },
    "Question2": {
        "Question": "What is the capital Japan?",
        "Answer": "Tokyo"
    },
    "Question3": {
        "Question": "What is the capital South Korean?",
        "Answer": "Seoul"
    },
    "Question4": {
        "Question": "What is the capital Spain ?",
        "Answer": "Madrid"
    },
    "Question5": {
        "Question": "What is the capital Taiwan ?",
        "Answer": "Taipei"
    },
}

score = 0
for key, value in quiz.items():
    print(value['Question'])
    answer = input("Answer: ")

    if answer.lower() == value['Answer'].lower():
        print("Correct \n")
        score = score + 1
        print("Your score is: ", score)

    else:
        print("Wrong")
        print("The answer is :" + value['Answer'] + "\n")
        print("Your score is " + str(score) + "\n")

print("You got" + str(score) + "out of 5 questions correctly \n ")

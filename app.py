import string


print("Welcome to the quiz!")

playing = input("Would you want to play? (Y/N): ")

def game_loop(question_Count):
    #Add your questions and answers here
    questions = ['What language is this written in?', 'How many questions are in this?']
    answers = ['Python', '2']

    current_Answer = input(questions[question_Count] + ": ")
    if current_Answer == answers[question_Count]:
        print("Correct!")
        question_Count += 1
        print("Moving on to the next question ")
        if question_Count >= len(questions):
            print("Youve completed the Quiz!")
            quit()
        game_loop(question_Count)
    elif current_Answer == "q" or current_Answer == "quit":
        print("Come back soon!")
        quit()
    else:
        print("That was not correct! Sorry!")
        question_Count += 1
        if question_Count >= len(questions):
            print("Youve completed the Quiz!")
            quit()
        game_loop(question_Count)



if playing != "y":
    print("Maybe next time!")
    quit()
else:
    print("Let's Start!")
    game_loop(0)
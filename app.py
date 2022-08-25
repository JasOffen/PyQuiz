import string


print("Welcome to the quiz!")

playing = input("Would you want to play? (Y/N): ")
Count = 0

def game_loop(question_Count):

    questions = ['Question 1', 'Question 2']
    answers = ['Answer 1', 'Answer 2']

    current_Answer = input(questions[question_Count] + ": ")
    if current_Answer == answers[question_Count]:
        print("Correct!")
        question_Count += 1
        print("Moving on to the next question ")
        print(question_Count)
        game_loop(question_Count)
    elif current_Answer == "q" or current_Answer == "quit":
        print("Come back soon!")
        quit()
    else:
        print("That was not correct! Sorry!")
        question_Count += 1
        game_loop(question_Count)
    
        

if playing != "y":
    print("Maybe next time!")
    quit()
else:
    print("Let's Start!")
    game_loop(Count)
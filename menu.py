import sys


# TASK 3:
# Create a Main Menu Welcome screen: 1. P to Play Quiz 2. A - About the Quiz  3. Q to Quit
# Play the program to see how it works. Can you add one more menu function?
##Fill in some information for 'About' and Start the Quiz (do one question)

def mainmenu():
    print("******************************** == WELCOME == ******************************")
    print("Press P to Play")
    print("Press A to find out more about the quiz")
    print("Press Q to Quit")
    print(" - - - - - - - - - - - - - - - - ")

    choice = input("Please enter your selection:")
    if choice == "p" or choice == "P":
        quiz()
    elif choice == "a" or choice == "A":
        about()


def quiz():
    print("*****WELCOME TO THE QUIZ***************")
    print(".....ready to play?!")


def about():
    print("About the quiz")
    print("This quiz is going to have x questions and will be on the topic .......")


def quit():
    print("Sorry to see you go ....Goodbye!")
    sys.exit()


mainmenu()
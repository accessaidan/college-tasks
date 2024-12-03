import random

def RPSgame():
    arr_rps = ['r','p','s']
    comp_choice = arr_rps[random.randint(0,2)]

    print("What will you choose")
    print("Rock [r]")
    print("Paper [p]")
    print("Scissors [s]")
    user_choice = input("").lower()

    if user_choice == comp_choice:
        print("DRAW")
        if user_choice == "r":
            user_choice = "Rock"
        if user_choice == "P":
            user_choice = "Paper"
        if user_choice == "s":
            user_choice = "Scissors"
        print("You both chose", user_choice)

    elif user_choice == "r":
        if comp_choice == "p":
            print("YOU LOSE")
            print("Unlucky, the AI beat you with Paper")
        elif comp_choice == "s":
            print("YOU WIN")
            print("The AI chose scissors")

    elif user_choice == "p":
        if comp_choice == "s":
            print("YOU LOSE")
            print("Unlucky, the AI beat you with Scissors")
        elif comp_choice == "r":
            print("YOU WIN")
            print("The AI chose Rock")

    elif user_choice == "s":
        if comp_choice == "r":
            print("YOU LOSE")
            print("Unlucky, the AI beat you with Rock")
        elif comp_choice == "p":
            print("YOU WIN")
            print("The AI chose Paper")
    
    again = input("would you like to play again?   [y/n]")
    if again == "y":
        RPSgame()

RPSgame()
    
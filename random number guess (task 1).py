import random


global num_ran
global attempts
global arr_guesses
num_ran = random.randint(1,100)

attempts = 0
arr_guesses = []

def num_guess():
    global num_ran
    global attempts
    global arr_guesses
    guess = int(input("What is your guess? "))
    

    if guess == num_ran:
        attempts = attempts + 1
        print("Congrats, you got it in", attempts)
        arr_guesses.append(guess)
        print("Your guess' went")
        print(arr_guesses)
    
    elif guess < num_ran:
        attempts = attempts + 1
        print("Your guess is too low")
        arr_guesses.append(guess)
        num_guess()
    
    elif guess > num_ran:
        attempts = attempts + 1
        print("Your guess is too high")
        arr_guesses.append(guess)
        num_guess()

num_guess()
import random

def get_input():
    user_input = input("Enter any number between 0-51: ")
    try:
        guess = int(user_input)
        return guess
    except ValueError:
        return "Enter an integer please"

def guessNum():
    number = random.randint(1,50)
    number_of_guesses = 0
    while number_of_guesses < 3:
        number_of_guesses += 1
        guess = get_input()
        if not isinstance(guess, int):
            print (guess)
        elif guess < 1 or guess > 50:
            print ("The number is out of range")
        elif guess < number:
            print (str(guess) + " guess is too low.")
        elif guess > number:
            print (str(guess) + " is too high.")
        elif guess == number:
            break
    if guess == number:
        print ("Yaay you nailed it! " + str(guess) + " is the right number")
    if guess != number:
        print ("Too bad, the right guess is " + str(number))
guessNum()

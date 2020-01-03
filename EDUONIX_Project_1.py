"""Guess the number:

1.)Create a script that'll ask the user how many games they would like to play.

2.)For every game ask the player to select a number between 1 to 25.

3.)Inform the player whether the number is higher or lower.

4.)Build a loop statement that'll iterate the number of players and the numbers picked.

5.)When the user guesses right, tell them how many guesses it took.

For every iteration we generate a random number, and take inputs from the user till he guesses the right number."""

import random
number_of_games=int(input("How many games would you like to play"))
for i in range(0,number_of_games):
    print("\n")
    random_number=random.randrange(1,25,1)
    user_number=int(input("Enter your guess"))
    guesses=0
    while(user_number!=random_number):
        guesses+=1
        if(user_number>random_number):
            print("Number high, decrease your guess")
            user_number=int(input("Enter your guess"))
        else:
            print("Number low, increase your guess")
            user_number=int(input("Enter your guess"))
    print("You took", guesses,"guesses and the guessed number is",random_number)

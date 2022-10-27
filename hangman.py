#Wordlist
#input with validation that letter is part of the word
#two player with counter leg/leg/arm/arm/torso/head = 5
import random

# wordlist
wlist =  ["fast", "slow", "left", "right", "down"]

# generate random word from list
hang_word = random.choice(wlist)
print(hang_word)

#introduction
print("Welcome to Hangman! Guess the word in less than 5 tries!")

guess = input("Please guess a single letter: ")
#store information for later
guess1 = guess

#input validation
if len(guess) == 1 and guess.isalpha():
    if guess in hang_word:
        print("indeed")
    else:
        print("wrong, guess again!")
else:
    print("pick a letter, bitch")


#check if guess is correct
answer = (guess1 + guess2 + guess3 + guess4)
while hang_word != answer:
    
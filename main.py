import random
import os
from turtle import right

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = [
    "Hangman",
    "cigarette",
    "news",
    "active",
    "distant",
    "faith",
    "utter",
    "blonde",
    "rob",
    "bitter",
    "spring",
    "option",
    "entry",
    "system",
    "tight",
    "separation",
    "proud",
    "cutting",
    "courage",
    "disappoint",
    "point",
]
word = random.choice(words)


guessCounter = 0
guesses = []
rightguess = 0
# fuck python
wasIn = []
while True:
    if guessCounter > 5:
        print(HANGMANPICS[6])
        print("YOU LOST")
        exit()


    print(HANGMANPICS[guessCounter])
    guessDisplayer = ""
    
    for char in word:
        if char in guesses:
            guessDisplayer += " " + char + " "
            if char not in wasIn:
                rightguess+=1
                wasIn.append(char)

        else:
            guessDisplayer += " _ "

    if rightguess + 1 == len(word) or  " _ " not in guessDisplayer:
        print("you won")
        exit()
    #idk thsi is a retarded way to check if the user has won
    
    print(guessDisplayer)
    print("gueesses:", " ".join(guesses))
    
    print("rigthguess",rightguess)
    guess = input("Guess: ")
    if len(guess) > 1:
        guess = input("Guess: ")
    
    
    guesses.append(guess)

    if word.rfind(guess) < 0:
        # why tf is there no ++ operator in this fucking language istg
        guessCounter  = guessCounter + 1

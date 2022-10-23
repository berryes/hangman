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
while True:
    if guessCounter > 5:
        print("you lost")
        exit()


    print(HANGMANPICS[guessCounter])
    print(word)
    guessDisplayer = ""

    wasIn = []
    for char in word:
        if char in guesses:
            if char not in wasIn:
                guessDisplayer += " " + char + " "
                wasIn.append(char)
                rightguess+=1
        else:
            guessDisplayer += " _ "

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

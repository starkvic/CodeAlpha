#Importing libraries
import random

print("Welcome to the simple text based hangman game")
play_choice = input("Would you like to play Y/N")

words = [
    "luminous",
    "paradox",
    "wander",
    "serendipity",
    "echo",
    "vivid",
    "catalyst",
    "whisper",
    "obscure",
    "momentum",
    "fracture",
    "horizon",
    "solace",
    "ember",
    "gravity",
    "mosaic",
    "pulse",
    "enigma",
    "drift",
    "resilient",
    "glimmer",
    "rift",
    "nomad",
    "tangle",
    "clarity",
    "flux",
    "haven",
    "reverie",
    "anchor",
    "bloom"
]


while(play_choice=="y"):
    print("Lets start")
    current_word = words[random.randint(0,len(words))]
    #print(f"your word is {current_word}")  //Helps debug to see the selected word
    guess=[]
    for i in current_word:
        guess.append("_ ")
    print("Your word is ","".join(guess), "and it has ",len(current_word),"letters \nLet the guessing begin")
    #print(guess) //For testing 
    lifes = 5
    win= False
    while(lifes>0):
        letter = input("Your letter=")
        condition = False
        for i in range(len(current_word)):
            if(letter==current_word[i] and letter!=guess[i]):
                guess[i]=str(letter)
                condition = True
                break
        if("".join(guess)==current_word):
            print("Congratulations, you've won")
            lifes=0
            win = True
        if(condition==False):
            lifes-=1
            print(f"Wrong Word\nLives remaining {lifes}...")
        print("".join(guess))
    if(win==False):
        print("Game Over")
        print("Your word was ",current_word)
        play_choice=input("Would you like to play again?Y/N")
    else:
        play_choice=input("Would you like to play again?Y/N")

print("see you again")
    

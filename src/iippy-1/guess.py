# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    print "Welcome to Guess the number by free" 
    global secret_number
    secret_number = random.randint(0,99)
    print secret_number
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    # main game logic goes here	
    guess_num = int(guess)
    print "Guess was", guess_num
    if guess_num == secret_number:
        print "Correct"
    elif guess_num >secret_number:
        print "Higher"
    else:
        print "Lower"

    
# create frame
f = simplegui.create_frame("Guess by free", 300, 300)

# register event handlers for control elements and start frame
f.add_input("Enter", input_guess, 100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric




# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# helper function to start and restart the game
def new_game(num_range):
    print "New Game, Guess the number, by free" 
    
    global secret_number
    global limit_step
    if (num_range == RANGE100):
        secret_number = random.randint(0,99)
        limit_step = 7
    elif (num_range == RANGE1000):
        secret_number = random.randint(0,999)
        limit_step= 10
    else:
        print "num_range error", num_range
        
    print "secret_number", secret_number
    print "Number of remaining guesses", limit_step

def range100():
    # button that changes the range to [0,100) and starts a new game 
    range_default()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game(RANGE1000)
 
def range_default():
    new_game(RANGE100)

# event proess    
def input_guess(guess):
    global limit_step
    if (limit_step == 0):
        print "Out of guess"
        range_default()
        return
    
    guess_num = int(guess)
    print "Guess was", guess_num
    
    if guess_num == secret_number:
        print "Correct"
        range_default()
        return 
    elif guess_num > secret_number:
        print "Higher"
    else:
        print "Lower"
   
    limit_step -= 1
    print "Number of remaining guesses", limit_step

   
# global variable
limit_step = 0
secret_number = 0

# rang num
RANGE100 = 'range100'
RANGE1000 = 'range1000'

# create frame
f = simplegui.create_frame("Guess by free", 500, 500)

# register event handlers for control elements and start frame
f.add_input("Enter a number:", input_guess, 200)
f.add_button("range [0,100)", range100, 200)
f.add_button("range [0,1000)", range1000, 200)

# init game
range_default()

f.start() 






#coding:UTF-8

#import simplegui

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# helper function to start and restart the game
def new_game(num_range):
    print ("新一轮游戏")
    
    global secret_number
    global limit_step
    if (num_range == RANGE100):
        secret_number = random.randint(0,99)
        limit_step = 7
    elif (num_range == RANGE1000):
        secret_number = random.randint(0,999)
        limit_step= 10
    else:
        print("num_range error" + num_range)
        
    print("秘密数字:"+ str(secret_number))
    my_print( "Number of remaining guesses:" + str(limit_step))

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
        my_print ("Out of guess")
        range_default()
        return
    
    guess_num = int(guess)
    my_print("Guess was" + str(guess_num))
    
    if guess_num == secret_number:
        compare_print("Correct")
        range_default()
        return 
    elif guess_num > secret_number:
        compare_print("Higher")
    else:
        compare_print("Lower")
   
    limit_step -= 1
    my_print("Num of remaining guesses:" + str(limit_step))

# output to GUI
def my_print(msg):
    label.set_text(msg)

def compare_print(msg):
    label_result.set_text(msg)
    
# global variable
limit_step = 0
secret_number = 0

# rang num
RANGE100 = 'range100'
RANGE1000 = 'range1000'

# create frame
f = simplegui.create_frame("猜数游戏 by free", 200, 500)

# register event handlers for control elements and start frame
f.add_input("Enter Num:\n", input_guess, 200)
f.add_button("range [0,100)", range100, 200)
f.add_button("range [0,1000)", range1000, 200)

label = f.add_label("left times")
label_result = f.add_label('compare result')

# init game
range_default()

f.start() 






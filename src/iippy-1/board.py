# -*- coding: utf-8 -*-
# draw by free

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Global Variables
canvas_width = 800
canvas_height = 600

def draw_again():
    global draw_obj_list
    global obj_type
    global obj_point
    global obj_color 
    global is_back
    global count
    draw_obj_list = []
    obj_type = "circle"
    obj_point = (-1,-1)
    obj_color = "red"
    is_back = False
    count = 0
    
    
def play_back():
    global is_back
    is_back = True    
    timer.start()
    global count
    count = 0
    
def set_draw_circle():
    set_draw_type("circle")

def set_draw_square():
    set_draw_type("square")

def set_draw_rectangle():
    set_draw_type("rectangle")

def set_draw_type(one_type):
    global obj_type
    obj_type = one_type

def draw_handler(canvas):
    global is_back
    if is_back:
        global draw_obj_list
        global count
        obj_list_len = len(draw_obj_list)
        for index in range(obj_list_len):
            if index < count:
                draw_one_obj(canvas, draw_obj_list[index][0], draw_obj_list[index][1], draw_obj_list[index][2])
        if count > obj_list_len:
            timer.stop()
    else:
        global obj_type
        global obj_color
        global obj_point
        if obj_point != (-1,-1):
            draw_one_obj(canvas, obj_point, obj_type, obj_color)

def draw_one_obj(canvas, obj_point, obj_type, obj_color):
    if obj_type == "circle":
        canvas.draw_circle(obj_point, 10, 5, obj_color)
    elif obj_type == "square":
        canvas.draw_polygon([(10, 10), (10, 20), (20, 20), (20, 10)], 1, obj_color)
    else:
        print "to finish"

# set color
def set_draw_red():
    set_draw_color("red")

def set_draw_blue():
    set_draw_color("blue")

def set_draw_green():
    set_draw_color("green")

def set_draw_color(one_color):
    global obj_color
    obj_color = one_color

def mouse_handler(points):
# where back draw, do not process mouse event
    global is_back
    if ~is_back:
        global draw_obj_list
        global obj_type
        global obj_color
        global obj_point
        draw_obj_list.append((points, obj_type, obj_color))
        obj_point = points
        
def tick():
    global count
    count += 1
    
frame = simplegui.create_frame('Painter by free', canvas_width, canvas_height)

button_circle = frame.add_button('circle', set_draw_circle, 50)
button_square = frame.add_button('square', set_draw_square, 50)
button_rectangle = frame.add_button('rectangle', set_draw_rectangle, 50)

button_red = frame.add_button('Red', set_draw_red, 100)
button_green = frame.add_button('Green', set_draw_green, 100)
button_blue = frame.add_button('Blue', set_draw_blue, 100)

button_back = frame.add_button('Back', play_back, 200)
button_again = frame.add_button('Again', draw_again,200)


frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, tick)

draw_again()
frame.start()



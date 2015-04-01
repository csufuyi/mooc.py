#coding:UTF-8
# draw by free

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Global Variables

canvas_width = 800
canvas_height = 600

draw_obj_list = []
obj_type = "circle"

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
    canvas.draw_circle((80, 100), 10, 5, 'Green')

    canvas.draw_polygon([(10, 10), (10, 20), (20, 20), (20, 10)], 1, 'Green')

# to do list set color


def mouse_handler(points):
    global draw_obj_list
    global obj_type
    draw_obj_list.append((points, obj_type, "red"))
    print draw_obj_list
        


frame = simplegui.create_frame('Painter by free', canvas_width, canvas_height)

button_circle = frame.add_button('circle', set_draw_circle, 50)
button_square = frame.add_button('square', set_draw_square, 50)
button_rectangle = frame.add_button('rectangle', set_draw_rectangle, 50)

frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw_handler)

frame.start()




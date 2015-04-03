# -*- coding: utf-8 -*-
# draw by free

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

def draw_again():
    global draw_obj_list
    global obj_type
    global obj_color 

    global is_back
    global count
    global multiply
    global base_count

    draw_obj_list = []
    obj_type = "circle"
    obj_color = "red"

    is_back = False
    count = 0
    multiply = 1
    base_count = 0
    
# 带倍率调节的定时器响应         
def tick():
    global base_count
    global count
    global multiply
    base_count += 1
    if base_count % multiply == 0:
        count += 1

# 回放按钮响应    
def play_back():
    global is_back
    global count
    is_back = True
    timer.start()
    count = 0

# 回放倍率设置
def change_multiply(input_text):
    global multiply
    multiply = int(input_text)

# 设置画图对象的形状
def set_draw_circle():
    set_draw_type("circle")

def set_draw_square():
    set_draw_type("square")

def set_draw_triangles():
    set_draw_type("triangles")

def set_draw_type(one_type):
    global obj_type
    obj_type = one_type

#  设置画图对象的颜色 
def set_draw_red():
    set_draw_color("red")

def set_draw_blue():
    set_draw_color("blue")

def set_draw_green():
    set_draw_color("green")

def set_draw_color(one_color):
    global obj_color
    obj_color = one_color

# 画图和重放功能
def draw_handler(canvas):
    global is_back
    global draw_obj_list
    global count
    obj_list_len = len(draw_obj_list)
    if is_back:
        for index in range(obj_list_len):
            if index < count:
                draw_one_obj(canvas, draw_obj_list[index][0], draw_obj_list[index][1], draw_obj_list[index][2])
        if count > obj_list_len:
            timer.stop()
    else:
        #画最近添加的点
        if obj_list_len != 0:
                draw_one_obj(canvas, draw_obj_list[-1][0], draw_obj_list[-1][1], draw_obj_list[-1][2])

def draw_one_obj(canvas, point, draw_type, color):
    if draw_type == "circle":
        canvas.draw_circle(point, 50, 5, color)
    elif draw_type == "square":
        a = point[0]
        b = point[1]
        width = 40 # For squares, width = height
        height = 40
        canvas.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)], 2, color)
    elif draw_type == "triangles":
        # Formula for equilateral triangles:
        a = point[0]
        b = point[1]
        width = 100
        canvas.draw_polygon([(a, b), (a + width, b), ((2 * a + width) / 2, b + width / 2 / math.tan(math.pi / 6))],
                            5, "Black", color)

# 记录鼠标点击过的形状列表
def mouse_handler(point):
    global is_back
    global draw_obj_list
    global obj_type
    global obj_color
    if not is_back:
        draw_obj_list.append((point, obj_type, obj_color))

frame = simplegui.create_frame('Painter by free', 800, 600)
button_again = frame.add_button('Again', draw_again,200)
button_circle = frame.add_button('circle', set_draw_circle, 50)
button_square = frame.add_button('square', set_draw_square, 50)
button_rectangle = frame.add_button('triangles', set_draw_triangles, 50)
button_red = frame.add_button('Red', set_draw_red, 100)
button_green = frame.add_button('Green', set_draw_green, 100)
button_blue = frame.add_button('Blue', set_draw_blue, 100)
button_back = frame.add_button('Play Back', play_back, 200)
inp = frame.add_input('Multiply', change_multiply, 50)    
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, tick)

draw_again()

frame.start()



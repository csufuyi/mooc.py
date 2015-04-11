# -*- coding: utf-8 -*-
# guess game client ai
# by free

#import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import time
import os

from multiprocessing.connection import Client

# global variable
count = 0
req_list = []
ai_type = 0

class GuessClientAI:
    def __init__(self, id, min, max):
        self.id = id
        self.min = min
        self.max = max
        
    def send_req(self,req):
        conn.send(req)

    def recv_res(self, res):
        print 'recv'

    def log_req(self, req):
        global req_list
        req_list.append(req)

    def set_min(self, min):
        self.min = min

    def set_max(self, max):
        self.max = max

    def set_current_num(self, num):
        self.curnum = num

    def get_current_num(self):
        return self.curnum 

    # strategy 1
    def get_random_number(self):
        return  random.randint(self.min, self.max)

    # stragegy 2
    def get_mid_number(self):
        return  (self.min +  self.max) / 2

    def send_strategy(self):
        # change stragegy
        global ai_type
        if ai_type == 0:
            num = self.get_mid_number()
        else:
            num = self.get_random_number()

        self.set_current_num(num)
        self.send_req(num)
        # log for redraw
        self.log_req(num)
        
    def process(self, res):
        if res == 'ok':
            self.send_strategy()
            return True 
        elif res == 'big':
            self.set_max(self.get_current_num()-1)
            self.send_strategy()
            return True 
        elif res == 'small':
            self.set_min(self.get_current_num()+1)
            self.send_strategy()
            return True 
        elif res == 'hit':
            print 'Good!you got it'
            return False 
        elif res == 'notimes':
            print 'Sorry!you have no times'
            return False 
        else:
            print 'check error'
            return False 

# ai type set
def ai_mid():
    global ai_type
    ai_type = 0

def ai_random():
    global ai_type
    ai_type = 1
    
# for redo draw
def tick():
    global count
    count += 1

# 回放按钮响应    
def play_back():
    global count
    count = 0
    timer.start()

# 画图和重放功能
def draw_handler(canvas):
    canvas.draw_line((0, 0), (0, 99*5), 10, 'Green') 
    global req_list
    print req_list
    global count
    req_list_len = len(req_list)
    for index in range(req_list_len):
        #print req_list
        if index < count and index != req_list_len-1:
            canvas.draw_line((index*50, req_list[index]*5), ((index+1)*50, req_list[index+1]*5), 2, 'Red') 
            
#        canvas.draw_polyline([(10, req_obj_list[-1][0],), (30, 20), (90, 70)], 10, 'Green') 
#               draw_one_obj(canvas, draw_obj_list[-1][0], draw_obj_list[-1][1], draw_obj_list[-1][2])
    if count > req_list_len:
        timer.stop()
 
def new_game():
    # db for req sequence
    global req_list
    req_list = []

    # game logic
    ai = GuessClientAI(os.getpid(), 0, 99)

    # request1: begin
    # response1: ok
    ai.send_req('begin')
       
    # request2: ai_number
    # response2: ai_result:big,small,hit
    loop = True
    while loop:
        res = conn.recv()
        print res
        loop = ai.process(res)

    # for draw slowly
    play_back()

if __name__ == '__main__':
    # conn managerment
    address = ('localhost', 6000)
    conn = Client(address, authkey='secret password')

    # UI managerment
    f = simplegui.create_frame("猜数游戏 AI", 800, 600)
    f.add_button("new game [0,100)", new_game, 200)
    f.add_button("play back", play_back, 200)
    f.add_button("ai mid", ai_mid, 200)
    f.add_button("ai random", ai_random, 200)
    f.set_draw_handler(draw_handler)
    timer = simplegui.create_timer(200, tick)
    f.start() 

    # conn end
    conn.close()





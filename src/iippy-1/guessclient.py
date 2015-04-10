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

class GuessClientAI:
    def __init__(self, id, min, max):
        self.id = id
        self.min = min
        self.max = max
        
    def send_req(self,req):
        conn.send(req)
        self.log_req(req)

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
        # num = self.get_random_number()
        num = self.get_mid_number()
        print num
        self.set_current_num(num)
        self.send_req(num)
    
    def process(self, res):
        if res == 'big':
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

# for redo draw
def tick():
    global count
    count += 1

# 画图和重放功能
def draw_handler(canvas):
    canvas.draw_line((0, 0), (0, 99), 10, 'Red') 
    global req_list
    req_list_len = len(req_list)
    for index in range(req_list_len):
        canvas.draw_polyline([(10, 20), (30, 20), (90, 70)], 10, 'Green') 
#               draw_one_obj(canvas, draw_obj_list[-1][0], draw_obj_list[-1][1], draw_obj_list[-1][2])

def new_game():
    # game logic
    ai = GuessClientAI(os.getpid(), 0, 99)

    # request: ai_number
    # response: ai_result:big,small,hit,notimes
    begin_num = ai.get_mid_number()
    print begin_num
    ai.set_current_num(begin_num)
    ai.send_req(begin_num)

    loop = True
    while loop:
        #time.sleep(1)
        res = conn.recv()
        print res
        loop = ai.process(res)
#        print "ai is working " + str(ai.id)

if __name__ == '__main__':
    # conn managerment
    address = ('localhost', 6000)
    conn = Client(address, authkey='secret password')

    # UI managerment
    f = simplegui.create_frame("猜数游戏 AI", 200, 200)
    f.add_button("new game [0,100)", new_game, 200)
    f.set_draw_handler(draw_handler)
    timer = simplegui.create_timer(100, tick)
    f.start() 

    # conn end
    conn.close()





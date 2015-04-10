# -*- coding: utf-8 -*-
# guess game client
# by free

#import simplegui
import random
import time
import os
from multiprocessing.connection import Client


class GuessClientAI:
    def __init__(self, id, min, max):
        self.id = id
        self.min = min
        self.max = max
        
    def send_req(self,req):
        conn.send(req)

    def recv_res(self, res):
        print 'recv'
        add_res(res)

    '''        
    def add_req(self, req):
        self.req_list.append(req)

    def add_res(self, res):
        self.res_list.append(res)

    def reset(self):
        self.req_list.clear()
        self.res_list.clear()
        self.min = 0
        self.max = 99 '''

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
            ai.set_max(ai.get_current_num()-1)
            ai.send_strategy()
            return True 
        elif res == 'small':
            ai.set_min(ai.get_current_num()+1)
            ai.send_strategy()
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

if __name__ == '__main__':
    # conn managerment
    address = ('localhost', 6000)
    conn = Client(address, authkey='secret password')

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
        print "ai is working " + str(ai.id)
        res = conn.recv()
        print res
        loop = ai.process(res)

    # conn end
    conn.close()
    print "ai is done " + str(ai.id)

# UI managerment
# create frame
#f = simplegui.create_frame("猜数游戏 AI", 200, 500)

# register event handlers for control elements and start frame
#f.add_button("range [0,100)", range100, 200)
#f.start() 






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
        
    def add_req(self, req):
        self.req_list.append(req)

    def add_res(self, res):
        self.res_list.append(res)

    def reset(self):
        self.req_list.clear()
        self.res_list.clear()
        self.min = 0
        self.max = 99

    def set_bound(self, min, max):
        self.min = min
        self.max = max

    def get_random_number(self):
        return  random.randint(self.min, self.max)
 

def range100():
    pass


# conn managerment
address = ('localhost', 6000)
conn = Client(address, authkey='secret password')

# game logic
ai = GuessClientAI(os.getpid(), 0, 99)
begin_num = ai.get_random_number()
ai.send_req(begin_num)


while True:
    print "ai is working" + str(ai.id)
    print time.ctime()
    time.sleep(1)
    
    res = conn.recv()
    print res
    ai.send_req(res)
conn.close()

# UI managerment
# create frame
#f = simplegui.create_frame("猜数游戏 AI", 200, 500)

# register event handlers for control elements and start frame
#f.add_button("range [0,100)", range100, 200)
#f.start() 






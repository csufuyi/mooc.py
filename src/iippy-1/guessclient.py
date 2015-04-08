# -*- coding: utf-8 -*-
# draw by free

#import simplegui
import random
import time

from multiprocessing.connection import Client
from array import array


class GuessClientAI:
    def __init__(self, id):
        self.id = id
        
    def send_req(req):
        print 'send req to server'

    def recv_res(res):
        print 'recv'
        add_res(res)
        
    def add_req(req):
        self.req_list.append(req)

    def add_res(res):
        self.res_list.append(res)

    def reset():
        self.req_list.clear()
        self.res_list.clear()
        self.min = 0
        self.max = 99

    def set_bound(min, max):
        self.min = min
        self.max = max

    def get_number():
        return  random.randint(self.min, self.max)
 

def range100():
    pass

# game logic
ai = GuessClientAI(1)
ai.send_req()


# conn managerment
address = ('localhost', 6000)
conn = Client(address, authkey='secret password')

while True:
    print "ai is working"
    print time.ctime()
    time.sleep(1)
    print conn.recv()                 # => [2.25, None, 'junk', float]

conn.close()

# UI managerment
# create frame
#f = simplegui.create_frame("猜数游戏 AI", 200, 500)

# register event handlers for control elements and start frame
#f.add_button("range [0,100)", range100, 200)
#f.start() 






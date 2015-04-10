# -*- coding: utf-8 -*-
# guessgame server
# by free

import random
import time
import os

from multiprocessing.connection import Listener
from multiprocessing import Process

class GuessServer:
    def __init__(self, id):
        self.id = id
        self.secret_num = random.randint(0,99)

    def send(self, conn, req):
        conn.send(req)

    def recv(self, conn, res):
        self.send (conn, res)

    def process(self, conn, res):
        print self.secret_num
        print res 
        req = 'haha'
        if res  == self.secret_num:
            req = 'hit'
        elif res > self.secret_num:
            req = 'big'
        else:
            req = 'small'
        self.send (conn, req)


# game logic
def game_proc(conn, id):
    server = GuessServer(id);
    print server.id
    while True:
        res =  conn.recv()
        server.process(conn, res)
    conn.close()


if __name__ == '__main__':

    # multiprocessing connection managerment
    print 'Parent process %s.' % os.getpid()
    address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
    listener = Listener(address, authkey='secret password')
    id = 0

    # one connection with a sub Process
    while True:
        conn = listener.accept()
        print 'connection accepted from', listener.last_accepted

        id += 1
        p = Process(target=game_proc, args=(conn, id,))

        print 'Process will start.' + str(id)
        p.start()

    # Listener end
    listener.close()
    print 'Process end.'



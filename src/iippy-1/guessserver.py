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
        
    def send(self, conn, req):
        conn.send(req)

    def recv(self, conn, res):
        self.send (conn, res)


# game logic
def game_proc(conn, id):
    while True:
        print time.ctime()
        time.sleep(1)
        server = GuessServer(id);
        print server.id
        res =  conn.recv()
        server.recv(conn, res)
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



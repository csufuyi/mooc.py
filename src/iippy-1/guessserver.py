#coding:UTF-8

import random
import time

from multiprocessing.connection import Listener
from array import array

class GuessServer:
    def __init__(self, id):
        self.id = id
        
    def send(self, req):
        conn.send(req)

    def recv(self, res):
        self.send (res)

# game logic
server = GuessServer(1);
address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey='secret password')
conn = listener.accept()
print 'connection accepted from', listener.last_accepted


while True:
    print "server is working"
    print time.ctime()
    time.sleep(1)

    res =  conn.recv()
    server.recv(res)


#conn.send([2.25, None, 'junk', float])
# conn managerment
conn.close()
listener.close()


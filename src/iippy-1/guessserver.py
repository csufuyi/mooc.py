#coding:UTF-8

import random
import time

from multiprocessing.connection import Listener
from array import array

class GuessServer:
    def __init__(self, id):
        self.id = id
        
    def send_req(req):
        print 'send req to server'

    def recv_res(res):
        print 'recv'

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
    print conn.recv()


#conn.send([2.25, None, 'junk', float])
# conn managerment
conn.close()
listener.close()


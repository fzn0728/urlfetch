# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 09:57:07 2016

@author: ZFang
"""

import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out
    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print("Finished Background file write to " + self.out)
        
def Main():
    message = input("Enter a string to store:")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print("The program can continute to run while it write in another thread")
    print(100+400)
    
    background.join()
    print("Waited until thread was complete")
    
if __name__ == '__main__':
    Main()
import sys
from time import sleep
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)
sys.stdout = Unbuffered(sys.stdout)
n=int(sys.argv[1])
if n <= 1: print "n must be greater than 1."; exit(1)
numbers=[]
repeat=[4, 2, 4, 2]
print "%s --> " %str(n),
while n != 1:
    if n == 2: print "1"; exit(1)
    if n%2 == 0: n=n/2
    else: n=(n*3)+1
    print "%s --> " %(str(n)),
    numbers.append(n)
    sleep(0.01)
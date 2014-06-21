
import time
import random

# Define SpeedTest class

class SpeedTest(object):
    """
        Test speed of your PC
        Calculating number of calculation per Second
    """
    def __init__(self):
    
        self.start_time = time.time()

    def operations(self):
        '''
            This function do lots of normal calculation & operation

                      TOTAL CALCULATION OR STEPS
                         100000*(12)=1200000
        '''
        for i in range(100000):
            x = random.randrange(1,99) # 1 FOR random number generation
            y = random.randrange(1,99) # 1 for assignment to x & y

            z = x+y   # 1 for add & 1 for assignment to z
            z = x-y   #  ''  ''  ''  ''  ''  ''  ''
            z = x*y   #  ''  ''  ''  ''  ''  ''  ''
            z = x/y   #  ''  ''  ''  ''  ''  ''  ''

        return 1200000 # total number of steps

    def __str__(self):
        """
            print style
        """
        time_interval = time.time()-self.start_time
        
        return str(int(self.operations()/time_interval))
    
if __name__=='__main__':
    print "http://beginer2cs.blogspot.com \n @Sudhanshu Patel"

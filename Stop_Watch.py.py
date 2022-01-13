'''
STOP WATCH Program

'''
print("  STOP WATCH   \n")

import time

def countdown(t):
    while t:
        mins,sec=divmod(t,60)  #pythone defined function used to divide the parameters. like min/sec
        timer='{:02d}:{:02d}'.format(mins,sec)
        print(timer,end="\r")
        time.sleep(1)
        t-=1 
    print("Time Up!")

t=int(input("Enter the no of seconds"))
countdown(t)

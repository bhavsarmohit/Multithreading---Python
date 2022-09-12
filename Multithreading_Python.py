import threading
import time

def printhello():
    i=0
    while(True):
        print('hello',i)
        # time.sleep(0.5)
        i+=1
        if(i==100):
            break

# receiveQuery()

# Create two threads as follows
try:
    # creating thread
    t1 = threading.Thread(target=printhello)
    t2 = threading.Thread(target=printhello)

    # starting thread 1
    t1.start()
    # starting thread 2
    time.sleep(0.3)
    t2.start()

    # wait until thread 1 is completely executed
    # t1.join()
    # wait until thread 2 is completely executed
    # t2.join()
except:
    print("Error: unable to start thread")

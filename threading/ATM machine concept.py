import threading
import time

BALANCE =100
lock = threading.Lock()

def withdraw():
    global BALANCE
    with lock:
        if BALANCE < 10:
            return
        time.sleep(1)
        BALANCE -= 10

if __name__ == '__main__':
    print("Initial balance {}".format(BALANCE))
    threads = []
    for _ in range(1010):
        thread = threading.Thread(target=withdraw)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("Balance left {}".format(BALANCE))
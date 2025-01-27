import threading
import time

MONEY = 0

def get_rich(iterations):
    lock = threading.Lock()
    global MONEY
    with lock:
        for n in range(iterations):
            MONEY += 1
    print('money ' + str(MONEY) + '$')

# expected money 1000$

if __name__ == '__main__':
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=get_rich, args=(100,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
print('final money ' + str(MONEY) + '$')
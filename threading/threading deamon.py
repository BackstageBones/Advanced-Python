import threading
import time


def daemon():
    print('Daemon Starting')
    time.sleep(2)
    print('Daemon Ending')


daemon_t = threading.Thread(name="daemon_t", target=daemon, daemon=True)


def non_daemon():
    print('Non-Daemon Starting')
    time.sleep(2)
    print('Non-Daemon Ending')


non_daemon_t = threading.Thread(name="non-daemon", target=non_daemon)

daemon_t.start()
non_daemon_t.start()

daemon_t.join()
non_daemon_t.join()
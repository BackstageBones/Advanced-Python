import threading
import time
from contextlib import contextmanager

import requests



gists = ['https://gist.github.com/recluze/1d2989c7e345c8c3c542',
         'https://gist.github.com/recluze/a98aa1804884ca3b3ad3',
         'https://gist.github.com/recluze/5051735efe3fc189b90d',
         'https://gist.github.com/recluze/460157afc6a7492555bb',
         'https://gist.github.com/recluze/5051735efe3fc189b90d',
         'https://gist.github.com/recluze/c9bc4130af995c36176d']


def get_gist(gist):
    response = requests.get(gist)
    response.raise_for_status()
    # print( "Size of gist in kB: {}".format(len(response.text)/1024))

@contextmanager
def timeit():
    start_time = int(round(time.time() * 1000))

    yield  # your function takes place here

    end_time = int(round(time.time() * 1000))
    elapsed = end_time - start_time
    print(f"Code took {elapsed} ms to run, or {elapsed/1000} seconds." )


if __name__ == '__main__':
    with timeit():
        for g in gists:
            get_gist(g)
        print("All done.")


    with timeit():
        threads = [threading.Thread(name='get_gist', target=get_gist, args=(gist, )) for gist in gists]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        print("All done.")

"""
All done.
Code took 573 ms to run.
All done.
Code took 105 ms to run.
"""

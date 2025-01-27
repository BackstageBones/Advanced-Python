import threading
import requests
import time
from functools import lru_cache

urls_to_check = ["https://www.google.com", "https://www.yahoo.com", "https://www.facebook.com", "https://www.instagram.com", "https://www.youtube.com"]
@lru_cache(maxsize=None)
def get_request(url):
    response = requests.get(url)
    print(threading.current_thread().name)
    assert response.raise_for_status()


start = time.time()
threads = [threading.Thread(name=url[12:], target=get_request, args=(url,)) for url in urls_to_check]


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
end = time.time()
print("Processing took {} seconds".format((end - start)))



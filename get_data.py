import threading

import requests

def get_city_url(id):
    return "https://secim-storage-cdn.ntv.com.tr/election2023/president/33.json?v=20230514092410"

def get_city_data(id):
    response = requests.get(get_city_url(id))
    print("Getting data for city {}".format(id))
    with open("data/{}.json".format(id), "w") as file:
        file.write(response.text)


threads = []

for i in range(1, 81):
    threads.append(threading.Thread(target=get_city_data, args=(i,)))
    threads[-1].start()

for thread in threads:
    thread.join()


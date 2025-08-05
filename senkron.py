import threading
import time
import requests

def get_data_sync(urls):
    st =time.time()
    json_array =[]
    for url in urls:
        json_array.append(requests.get(url).json())
    et=time.time()
    elapsed = et - st
    print("Execution time: ", elapsed, "seconds")
    return json_array
urls = ["https://postman-echo.com/delay/3"] * 10
get_data_sync(urls)
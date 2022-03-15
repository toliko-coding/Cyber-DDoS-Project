
import threading
import time
from timer import timer

import requests
from requests.structures import CaseInsensitiveDict

# Define a function for the thread

url = "http://127.0.0.1/"

"TEST2"
headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer mt0dgHmLJMVQhvjpNXDyA83vA_PxH23Y"
headers["Content-Type"] = "application/json"


data = """
{
  "Id": 12345,
  "Customer": "John Smith",
  "Quantity": 1,
  "Price": 10.00
}
"""
def T1():
    while True:
        resp1 = requests.post(url, headers=headers, data=data)
        print("T1")
        print(resp1.status_code)
        print(threading.active_count())
        T1()









# def T2():
#     while True:
#         resp = requests.post(url, headers=headers, data=data)
#         print(resp.status_code)
#         print("T2")
#         time.sleep(0.01)




#Create two threads as follows
try:

   x = threading.Thread(T1())
   #y = threading.Thread*T2()

   x.start()
   #y.start()





except:
   print ("Error: unable to start thread")

while 1:
   pass


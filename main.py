import requests
from requests.structures import CaseInsensitiveDict

url = "http://127.0.0.1/hello.html"

"TEST"
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
i = False
while i is not True:
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)


#!/usr/bin/env python3
from datetime import datetime
import requests

today = datetime.now().strftime("%Y-%m-%d")
url = f"https://www.nytimes.com/svc/wordle/v2/{today}.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  
    print(f"today wordle solution is: {data['solution']}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")



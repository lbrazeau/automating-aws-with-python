# coding: utf-8
import requests
url = '' # Replace with slack webhook URL
data = { "text": "Hello, LB1." }
requests.post(url, json=data)

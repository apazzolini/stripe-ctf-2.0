import requests

response = requests.post('http://localhost:9233/orders', data='')

print response.text

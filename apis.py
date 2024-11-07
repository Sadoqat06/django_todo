import requests

# response = requests.get('https://randomuser.me/api/').json()
response = requests.get('https://fakestoreapi.com/products').json()

print(response)




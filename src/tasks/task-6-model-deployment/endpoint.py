import requests

auth = ('ampaduh@gmail.com', 'pass1234')
login_response = requests.get('http://127.0.0.1:5000/user/login', auth =auth)
print(login_response.text)
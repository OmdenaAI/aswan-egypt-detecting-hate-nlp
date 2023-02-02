import requests
from dotenv import load_dotenv
import os

load_dotenv()

auth = (os.environ.get("AUTHENTICATE_USERNAME"), os.environ.get("AUTHENTICATE_PASSWORD"))
login_response = requests.get('http://127.0.0.1:5000/user/login', auth =auth)
print(login_response.text)
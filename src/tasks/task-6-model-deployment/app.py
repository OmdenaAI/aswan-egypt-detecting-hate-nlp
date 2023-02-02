from flask import Flask, render_template, request, jsonify, make_response
import jwt
import psycopg2
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["DBNAME"] = os.environ.get("DBNAME")
app.config["DBUSER"] = os.environ.get("DBUSER")
app.config["DBPASSWORD"] = os.environ.get("DBPASSWORD")
app.config["DBPORT"] = int(os.environ.get("DBPORT"))
app.config["SECRET_KEY"] = os.environ.get("AUTHSECRET")
             



@app.route("/")
def hello_world():
    return render_template('/home.html')


@app.route("/user/login")
def user_login():
    #if user cannot be found
    auth = request.authorization
    if not auth:
        return "missing credentials", 401

    #connect to postgreSQL database
    conn = psycopg2.connect(dbname=app.config["DBNAME"],user=app.config["DBUSER"],
            password=app.config["DBPASSWORD"], port = app.config["DBPORT"])
    cur = conn.cursor()
    
    #check for username and password in database
    cur.execute(
            f"SELECT * FROM users;", 
             ) 
    row = cur.fetchone() 

    #if there's a user
    if len(row) > 1:  
        email = row[1]
        password = row[2]

        if auth.username != email or auth.password != password:
            return "invalid credentials", 401
        else:
            token = jwt.encode({'username':auth.username, 'exp':datetime.utcnow()+ timedelta(minutes=10),'alg':"HS256"},app.config["SECRET_KEY"])
            return jsonify({'token':token})
    else:
        return "user missing credentials", 401



if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, render_template, request, jsonify, make_response
import jwt
# import psycopg2
from datetime import datetime, timedelta
# from dotenv import load_dotenv
import os
from transformers import DistilBertTokenizer, TFDistilBertModel
from keras.models import load_model
import numpy as np

# load_dotenv()

app = Flask(__name__)

# app.config["DBNAME"] = os.environ.get("DBNAME")
# app.config["DBUSER"] = os.environ.get("DBUSER")
# app.config["DBPASSWORD"] = os.environ.get("DBPASSWORD")
# app.config["DBPORT"] = int(os.environ.get("DBPORT"))
# app.config["SECRET_KEY"] = os.environ.get("AUTHSECRET")

trained_model = load_model("./DL_model_DistilBert_Lstm.h5", custom_objects = {'TFDistilBertModel': TFDistilBertModel})

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
bert_model = TFDistilBertModel.from_pretrained('distilbert-base-uncased')
MAX_LEN = 128


@app.route("/")
def hello_world():
    return render_template('/home.html')

@app.route("/check-statement", methods = ['POST'])
def check_statement():
    print('Got the hit!!')
    data = request.form
    text_tokenized = tokenizer.encode_plus(
        data['text'],
        max_length=MAX_LEN,
        padding='max_length',
        truncation=True,
        return_token_type_ids=False,
        return_tensors='tf'
    )
    print('Tokenized Text has been generated!')
    prediction = trained_model.predict([text_tokenized['input_ids'].numpy()])
    print('Prediction done!')
    pred = np.argmax(prediction)
    print('got max probable class done!')
    print('pred', pred)
    return {'Status:': True, 'prediction': int(pred)}


# @app.route("/user/login")
# def user_login():
#     #if user cannot be found
#     auth = request.authorization
#     if not auth:
#         return "missing credentials", 401

#     #connect to postgreSQL database
#     conn = psycopg2.connect(dbname=app.config["DBNAME"],user=app.config["DBUSER"],
#             password=app.config["DBPASSWORD"], port = app.config["DBPORT"])
#     cur = conn.cursor()
    
#     #check for username and password in database
#     cur.execute(
#             f"SELECT * FROM users;", 
#              ) 
#     row = cur.fetchone() 

#     #if there's a user
#     if len(row) > 1:  
#         email = row[1]
#         password = row[2]

#         if auth.username != email or auth.password != password:
#             return "invalid credentials", 401
#         else:
#             token = jwt.encode({'username':auth.username, 'exp':datetime.utcnow()+ timedelta(minutes=10),'alg':"HS256"},app.config["SECRET_KEY"])
#             return jsonify({'token':token})
#     else:
#         return "user missing credentials", 401



if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
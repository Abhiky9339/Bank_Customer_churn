from flask import Flask, render_template, request
import sqlite3
import logging

#initialize logging
LOG_FILE_NAME = 'LoanAppLog.txt'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=LOG_FILE_NAME,
                    filemode='w')

#initialize ml model
from joblib import dump, load
# load the saved model
loan_app = load('Bank_customer_churn.joblib')

# REST API service
app = Flask(__name__)
@app.route('/',methods=['POST', 'GET'])
def home():
    home_page = '<html><h1>Bank Customer churn PAGE</h1><body><a href="/application.html">Click here to check bank customer churn prediction</a></html>'
    return home_page

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

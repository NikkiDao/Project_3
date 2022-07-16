import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, jsonify

engine = create_engine('sqlite:///sql/streaming_db.sqlite')
conn = engine.connect()

netflix = engine.execute('SELECT * FROM netflix')
amazonprime = engine.execute('SELECT * FROM amazonprime')
disneyplus = engine.execute('SELECT * FROM disneyplus')
hulu = engine.execute('SELECT * FROM hulu')


app = Flask(__name__)

@app.route('/')
def home():
    print('testing')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
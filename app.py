import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, request, render_template, jsonify, make_response, redirect
import os 
import re

engine = create_engine('sqlite:///sql/streaming_db.sqlite')
conn = engine.connect()

netflix = engine.execute('SELECT * FROM netflix')
amazonprime = engine.execute('SELECT * FROM amazonprime')
disneyplus = engine.execute('SELECT * FROM disneyplus')
hulu = engine.execute('SELECT * FROM hulu')


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)



app = Flask(__name__)

@app.route('/')
def home():
    print('testing')
    return render_template('index.html')


# @app.route("/", methods=['GET', 'POST'])
# def index(): 
#     tab = ''
#     df_titles = pd.DataFrame()
#     if request.method == 'POST':
#         query = request.form['media_title']
#         if query != '':
#             df_titles = lookup(query)
#             tab = 'search'
#     streaming_db = get_dataframe_from_db('streaming_db')
#     return render_template("index.html", titles=df_titles.to_dict(orient='records'), streaming_services=streaming_db.to_dict(orient='records'), accessToken=accessToken, tab=tab)

# @app.route("/search")
# def search(): 
#     return render_template("search.html") 


if __name__ == '__main__':
    app.run(debug = True)
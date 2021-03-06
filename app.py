from flask import Flask, render_template
from config import app_key
import requests
import pandas as pd
from sqlalchemy import create_engine
app = Flask(__name__)


# create my own API from the data stored in Postgres database
@app.route('/get_weather')
def hello():
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/weather')
    df = pd.read_sql_table("weather_forecast",con=engine)
    return df.to_json()
# load the index.html when requesting the https://localhost:5000
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
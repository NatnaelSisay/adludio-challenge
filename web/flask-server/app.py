from flask import Flask
from flask_cors import CORS, cross_origin

import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join('../..')))

from my_scripts.helper import best_performers, read_csv

app = Flask(__name__)
CORS(app)

FILE_PATH   = '../../data/impression_log.csv'
CAMPAIN_ID  = 'CampainId'
SITE        = 'Site'

# Route to send all CamapinID's
@app.route("/")
def campains():
    df = read_csv(FILE_PATH)
    campain_ids = df[CAMPAIN_ID]
    unique_campain_ids = set(campain_ids)

    return {CAMPAIN_ID: list(unique_campain_ids)}


# Route to send Top scoring websites
@app.route('/<campian_id>')
def campain(campian_id):
  df = pd.read_csv(FILE_PATH)
  result = best_performers(df, campian_id)[SITE]

  return {f"{campian_id}": list(result)}
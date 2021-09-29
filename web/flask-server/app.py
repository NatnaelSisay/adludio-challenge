from flask import Flask
from flask_cors import CORS, cross_origin

import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join('../..')))

from my_scripts.helper import best_performers, read_csv

app = Flask(__name__)
CORS(app)

file_path = '../../data/impression_log.csv'

# Route to send all CamapinID's
@app.route("/")
def campains():
    df = read_csv(file_path)
    campain_ids = df['CampaignId']
    unique_campain_ids = set(campain_ids)
    return {'CampainId': list(unique_campain_ids)}


# Route to send Top scoring websites
@app.route('/<campian_id>')
def campain(campian_id):
  df = pd.read_csv(file_path)
  result = best_performers(df, campian_id)["Site"]

  return {f"{campian_id}": list(result)}
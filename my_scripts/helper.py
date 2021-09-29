import pandas as pd


def best_performers(df, campain_id):
    df = df.copy()
    
    campains_score = df.groupby('CampaignId').get_group(campain_id)
    selcted_campain = campains_score.groupby('Site').agg({'engagement': 'sum', 'LogEntryTime':'count'})
    selcted_campain.rename(columns={'LogEntryTime': 'engagement-count'}, inplace=True)
    
    # method - 1
    # selcted_campain['score'] = selcted_campain['engagement'] / selcted_campain['engagement-count']
    
    #method - 2
    selcted_campain['score'] = (selcted_campain['engagement'] ** 2) / selcted_campain['engagement-count']
    
    result = selcted_campain.sort_values(by='engagement', ascending=False).reset_index()
    
    return result


def read_csv(file_path):
  try:
    df = pd.read_csv(file_path)
    return df
  except FileNotFoundError as e:
    print(e)
    return {"ERROR": "File path Not Correct"}

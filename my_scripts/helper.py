import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression


def best_performers(df, campain_id):
    '''
    Return DataFrame ordered by score value
      columns: engagement, engagement-count, score

    score = engagement ** 2 / engagement-count
    '''

    df = df.copy()
    
    campains_score = df.groupby('CampaignId').get_group(campain_id)
    selcted_campain = campains_score.groupby('Site').agg({'engagement': 'sum', 'LogEntryTime':'count'})
    selcted_campain.rename(columns={'LogEntryTime': 'engagement-count'}, inplace=True)
    
    #method - 1
    selcted_campain['score'] = selcted_campain['engagement'] / selcted_campain['engagement-count']
    
    #method - 2
    # selcted_campain['score'] = (selcted_campain['engagement'] ** 2) / selcted_campain['engagement-count']
    
    result = selcted_campain.sort_values(by=['engagement', 'score'], ascending=False).reset_index()
    
    return result


def read_csv(file_path):
  '''
  Return DataFrame with the provided file path
  '''
  try:
    df = pd.read_csv(file_path)
    return df
  except FileNotFoundError as e:
    print(e)
    return {"ERROR": "File path Not Correct"}


def bar_plot(x, y, df):
  '''
    Plot Bar chart 
  '''
  plt.figure(figsize=(12,6))
  plt.xticks(rotation=20)
  sns.barplot(x=x, y=y, data=df)


def oneHotEncoder(df, catagorical_columns):
    new_df = df.copy()
    new_df = pd.get_dummies(new_df, columns=catagorical_columns)
    return new_df


def labelEncoder(df,catagorical_columns):
    new_df = df.copy()
    for column in catagorical_columns:
            new_df[column] = LabelEncoder().fit_transform(new_df[column])
    return new_df


def train_model(train, test, model_type='Linear'):
    model = LinearRegression()
    
    if (model_type == 'Logistic'):
        model = LogisticRegression()
        
    model.fit(train, test)
    return model


def test_model(x_test, y_test, model):
    score = model.score(x_test, y_test)
    print("Model Score => ", score)


def logistic_featuer_importance(model, columns):
    importance = model.coef_[0]
    df = pd.DataFrame([list(importance)], columns=columns)
    df = df.transpose()
    df = df.reset_index()
    df.rename(columns={'index':'columns', 0:'score'}, inplace=True)
    return df


def linear_feature_importance(model, columns):
    importance = model.coef_
    df = pd.DataFrame([list(importance)], columns=columns)
    df = df.transpose()
    df = df.reset_index()
    df.rename(columns={'index':'columns', 0:'score'}, inplace=True)
    return df

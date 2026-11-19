import pandas as pd

def read_data():
    df = pd.read_csv("dataset_train.csv")
    print(df.head())
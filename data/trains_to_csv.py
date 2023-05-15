
import pandas as pd

train_data = pd.read_json('./trains.json')
train_data.to_csv('./trains.csv', index=False, header=False)

import pandas as pd
from trainitalia import viaggiatreno as vt
from tqdm import tqdm

df = pd.read_json('./data/trains.json')
print(df.head())
# df['Trip'] = [[] for i in range(len(df))]

for index, row in tqdm(df.iterrows(), total=len(df)):
    try:
        if len(row['Trip']) == 0:
            number, station, date = vt.get_train_start(row['ID'])
            stops = vt.trip_info(station, row['ID'])
            trip = []
            for stop in stops:
                trip.append(stop['id'])
            df.at[index, 'Trip'] = trip
    except:
        pass

df.to_json('./data/trains.json')
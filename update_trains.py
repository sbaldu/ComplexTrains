import pandas as pd
from trainitalia import viaggiatreno as vt
from tqdm import tqdm

df = pd.read_json('./data/trains.json')
print(df.head())
df['Trip'] = [[[]] for i in range(len(df))]

for index, row in tqdm(df.iterrows(), total=len(df)):
    try:
        trips = []
        for train in vt.get_start_info(row['ID']):
            number, station, date = train
            stops = vt.get_trip_info(number, station)
            trip = []
            for stop in stops:
                trip.append(stop['id'])
            trips.append(trip)
        df.at[index, 'Trip'] = trips
    except:
        pass

df.to_json('./data/trains.json')
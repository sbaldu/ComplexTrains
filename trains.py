from trainitalia import viaggiatreno as vt
import geopandas as gpd
from tqdm import tqdm

gdf = gpd.read_file("./data/stations.geojson")

filtered = gdf[gdf['cityName'] != 'A']
filtered = filtered[filtered['RegionID'] != '']

important = filtered[(filtered['Type'] == 1) | (filtered['Type'] == 2)]

categories = []
numbers = []
with open("./data/trains.txt", 'w') as fp: # maybe it is better to use a json file
    for index, row in tqdm(filtered.iterrows(), total=len(filtered)):
        for index2, row2 in tqdm(important.iterrows(), total=len(important)-1, leave=False):
            if index2 != index:
                trains = vt.get_solutions(row['ID'], row2['ID'])['soluzioni']
                try:
                    for train in trains:
                        category = train['vehicles'][0]['categoriaDescrizione']
                        number = train['vehicles'][0]['numeroTreno']
                        if number not in numbers:
                            categories.append(category)
                            numbers.append(number)
                            fp.write('{}|{}\n'.format(category,number))
                except:
                    pass

#  77%|████████████████████████████████████████████████████████████▍                  | 327/427 [2:14:31<41:08, 24.68s/it]
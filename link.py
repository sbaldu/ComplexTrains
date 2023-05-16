import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString
import pylab as plt
import torch

def find_index(station_id:str) -> int:
    '''prova a usare cript, atrimenti None'''
    try:
        io = cript[station_id]
    except(KeyError):
        io = None
    return io

#station e trains fittizzi per il codice
stat = [('S001', 'A', '1.00000', '1.00000'),
        ('S010', 'B', '2.00000', '1.00000'),
        ('S1001', 'C', '2.00000', '2.00000'),
        ('S01010', 'D', '1.00000', '2.00000')]
stations = pd.DataFrame(stat, columns=['ID', 'NAME', 'X', 'Y'])
geometry = [Point(xy) for xy in zip(stations['X'], stations['Y'])]
stations = gpd.GeoDataFrame(stations, geometry=geometry)
tr = [(['S001', 'S010'], '1'),
      (['S1001', 'S01010'], '2')]
trains = pd.DataFrame(tr, columns=['Trip', 'Name'])

# stations = gpd.read_file('stations.geojson') #stations vero
lenght = stations.shape[0]
cript = {}
i = 0
for identification in stations['ID']:
    cript[identification] = i
    i += 1

decript = {num: station for num, station in enumerate(cript)}



# trains = pd.read_json('trains.json') #trains vero

#crea matrice di adiacenza
link = torch.zeros((lenght, lenght), dtype=torch.bool)
for train in trains['Trip']:
    if train == []:
        continue
    station_1 = train[0]
    stat_1 = find_index(station_1)
    for station_2 in train[1:]:
        stat_2 = find_index(station_2)
        if stat_1 != None and stat_2 != None:
            link[stat_1, stat_2] = True
            # link[stat_2, stat_1] = True #triangular matrix
            stat_1 = stat_2
        elif stat_2 == None:
            continue
        elif stat_1 == None:
            stat_1 = stat_2

#crea dataframe dei link
mask = (link == True).nonzero(as_tuple=False).tolist()
mylist = []
for i, value in enumerate(mask):
    stat_1, stat_2 = value
    station_1 = decript[stat_1]
    station_2 = decript[stat_2]
    # print(station_1, station_2)
    coo_1 = stations.loc[stations['ID'] == station_1].iloc[0]['geometry']
    coo_2 = stations.loc[stations['ID'] == station_2].iloc[0]['geometry']
    print(coo_1) #point
    a = LineString(tuple(coo_1.coords) + tuple(coo_2.coords))
    mylist.append(a)
geo_link = pd.DataFrame(mylist, columns=['geometry'])
geo_link = gpd.GeoDataFrame(geo_link, geometry='geometry')

#stampa
fig, ax = plt.subplots()
stations.plot(ax=ax, marker= 'o', markersize=1)
geo_link.plot(ax=ax)
plt.show()

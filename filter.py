import geopandas as gpd

gdf = gpd.read_file('raw.geojson')

print(len(gdf))

# discard poitns without coordinates from dataset
gdf = gdf[gdf['Latitude'].notna()]
gdf = gdf[gdf['Longitude'].notna()]

print(len(gdf))

gdf.to_file('cleaned.geojson', driver='GeoJSON')

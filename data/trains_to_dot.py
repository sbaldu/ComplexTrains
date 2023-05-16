import pandas as pd

data = pd.read_json('./trains.json')

# Open dot file
f = open('stations.dot', 'w')
f.write("graph network_of_stations {\n")

for trip in data['Trip']:
    stations_pairs = list(zip(trip, trip[1:]))
    for pair in stations_pairs:
        f.write(f"\t{pair[0]} -- {pair[1]};\n")

f.write("}")
# Close dot file
f.close()

# Now remove repeated lines in the dot file
file = open('stations.dot', 'r')
file_lines = file.readlines()
file.close()

file_lines = [file_lines[0]] + list(set(file_lines[1:-1])) + [file_lines[-1]]
file = open('stations.dot', 'w')
for line in file_lines:
    file.write(line)
file.close()

from plotly.graph_objs import Scattergeo, Layout
import json
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)




#readable_file = 'data/readable_eq_data.json'
#with open(readable_file, 'w') as f:
#    json.dump(all_eq_data, f, indent=4)


all_eq_dic=all_eq_data['features']
print(len(all_eq_dic))

#to get the magintude from eq
magnitudes=[]
for eq_dic in all_eq_dic:
    magnitude=eq_dic['properties']['mag']
    magnitudes.append(magnitude)

#print(magnitudes[:10])


#extracting Location Data
longitudes,latitudes=[],[]# we could have put it with above and for loop but for you to understand
for eq_dic in all_eq_dic:
    longitude=eq_dic['geometry']['coordinates'][0]
    latitude=eq_dic['geometry']['coordinates'][1]
    longitudes.append(longitude)
    latitudes.append(latitude)

print(longitudes[:5])
print(latitudes[:5])
print(magnitudes[:10])

data = [Scattergeo(lon=longitudes,lat=latitudes)]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)





#readable_file = 'data/readable_eq_data.json'
#with open(readable_file, 'w') as f:
#    json.dump(all_eq_data, f, indent=4)


all_eq_dic=all_eq_data['features']
print(len(all_eq_dic))

#to get the magintude from eq
mags,lons,lats,hover_texts=[],[],[],[]
for eq_dic in all_eq_dic:
    title = eq_dic['properties']['title']
    lon=eq_dic['geometry']['coordinates'][0]
    lat=eq_dic['geometry']['coordinates'][1]
    mag=eq_dic['properties']['mag']
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
    hover_texts.append(title)






print(lons[:5])
print(lats[:5])
print(mags[:10])

# Map the earthquakes.
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text': hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'},

        },
    }]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

#other colors
#from plotly import colors
#for key in colors.PLOTLY_SCALES.keys():
#print(key)

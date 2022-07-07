import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    

#To make it easier to understand the file header data, we print each header and its postion in list
    for index, column_header in enumerate(header_row):
        print(index,column_header)


#Extracting and Reading Data
    
    # Get dates,high and low temperatures from this file.
    dates, highs, lows=[], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        low=int(row[6])
        high=int(row[5])#take the index 5 for tmax and convert it to number
        dates.append(current_date)
        lows.append(low)
        highs.append(high)
#print(highs)


#Plotting Data in a Temperature Chart

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)#alpha is for color transperancy
ax.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)#facecolor determines the 
#color of the shaded region
# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
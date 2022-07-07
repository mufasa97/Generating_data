

import matplotlib.pyplot as plt
plt.style.available

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.style.use('seaborn')
fig, ax=plt.subplots()
ax.plot(input_values,squares,linewidth=3)

# Set chart title and label axes.
ax.set_title("square numbers",fontsize=24)
ax.set_xlabel("value",fontsize=14)
ax.set_ylabel("square of value",fontsize=14)

#set size of tick label
ax.tick_params(axis='both',labelsize=14)



plt.show()
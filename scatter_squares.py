
import matplotlib.pyplot as plt

#x_values=[1,2,3,4,5]
#y_values=[1,4,9,16,25]
x_values=range(1,1001)
y_values=[x**2 for x in x_values]



plt.style.use('seaborn')
fig, ax=plt.subplots()
ax.scatter(x_values,y_values,s=10)

ax.set_title('square nummbers',fontsize=24)
ax.set_xlabel('value',fontsize=14)
ax.set_ylabel('squaer of value',fontsize=14)

ax.tick_params(axis='both',which='major',labelsize=14)

#set the range for each axis
ax.axis([0,1100,0,1100000])

plt.show()

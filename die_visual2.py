
from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die

#create two D6 dice 
die_1=Die()
die_2=Die()

# Make some rolls, and store results in a list.
results=[]
for roll_num in range(1000):
        result=die_1.roll()+ die_2.roll()
        results.append(result)

#analyze the results
frequencies=[]
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#print(frequencies)
    
#print(results)


#visualize the results
x_values=list(range(2,max_result+1)) #plotly doesn't accept value from range directly so we put it in a list
data = [Bar(x=x_values, y=frequencies)]  
#The Plotly class Bar() represents a data set that will be formatted as a bar chart
#The class must be wrapped in square brackets, because a data set can have multiple elements


x_axis_config={'title': 'Result'} # dtick controls the spacing between tick marks on x axis
y_axis_config={'title': 'Frequency fig Result'}
my_layout=Layout(title='Results of rolling two D6 1000 times',xaxis=x_axis_config,yaxis=y_axis_config)
#The Layout() class returns an object that specifies the layout and configuration of the graph as a whole


offline.plot({'data':data,'layout':my_layout},filename='d6_d6.html')
#To generate the plot, we call the offline.plot() function
#This function needs a dictionary containing the data and layout objects, and it also-
#-accepts a name for the file where the graph will be saved

from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die

#create a D6 
die=Die()

# Make some rolls, and store results in a list.
results=[]
for roll_num in range(1000):
        result=die.roll()
        results.append(result)

#analyze the results
frequencies=[]
for value in range (1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#print(frequencies)
    
#print(results)


#visualize the results
x_values=list(range(1,die.num_sides+1)) #plotly doesn't accept value from range directly so we put it in a list
data = [Bar(x=x_values, y=frequencies)]  
#The Plotly class Bar() represents a data set that will be formatted as a bar chart
#The class must be wrapped in square brackets, because a data set can have multiple elements


x_axis_config={'title': 'Result'}
y_axis_config={'title': 'Frequency fig Result'}
my_layout=Layout(title='Results of rolling one D6 1000 times',xaxis=x_axis_config,yaxis=y_axis_config)
#The Layout() class returns an object that specifies the layout and configuration of the graph as a whole


offline.plot({'data':data,'layout':my_layout},filename='d6.html')
#To generate the plot, we call the offline.plot() function
#This function needs a dictionary containing the data and layout objects, and it also-
#-accepts a name for the file where the graph will be saved

import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:   #to make multiple random walk

    #make the randomwalk
    rw=RandomWalk()#50000 t0 increase number of points but the defult is 5000
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    point_numbers=range(rw.num_points)
    fig, ax=plt.subplots(figsize=(15,9),dpi=100)# figsize() is to resize the figure to fit the map 
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)

    # Emphasize the first and last points.
    ax.scatter(0,0,c='green',edgecolors='none',s=100,)#,zorder=2) to make ontop of the element#first point (0,0)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)#last point

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ") #for the multiple random work
    if keep_running=='n':
        break


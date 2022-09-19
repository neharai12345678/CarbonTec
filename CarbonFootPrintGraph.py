# Import libraries
from matplotlib import pyplot as plt
import numpy as np
# import required modules
import pandas as pd
import matplotlib.pyplot as plt
def PlotCo2Print():
    # defining labels
    activities = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday']
    
    # portion covered by each label
    slices = [3, 7, 8, 6,1,2,5]
    
    # color for each label
    colors = ['b', 'r', 'r', 'b','g','g','y']
    
    # plotting the pie chart
    plt.pie(slices, labels = activities, colors=colors, 
            startangle=90, shadow = True, explode = (0, 0, 0.1, 0,0.1,0,0.1),
            radius = 1.2, autopct = '%1.1f%%')
    
    # plotting legend
    plt.legend()
    
    # showing the plot
    plt.show()
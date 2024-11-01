import matplotlib.pyplot as plt   

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y) # creates a line plot of y-axis  values against x- values

plt.xlabel('X-axis') 
plt.ylabel('Y-axis')
plt.title('Simple Line Plot') #gives the heading of the graph

plt.show() #output window
import matplotlib.pyplot as plt  # pyplot module as plt 

x = [1, 2, 3, 4, 5] # giving x and y values 
y = [5, 7, 8, 9, 12]

plt.scatter(x, y, color='red') # creates scatterplot with x and y values 

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')

plt.show()
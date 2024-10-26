import numpy as np #importing numpy as np 

X = np.array([1, 2, 3, 4, 5]) # giving data, x is input data
y = np.array([1, 2, 3, 4, 5])#labels,targer data

X_b = np.c_[np.ones((len(X), 1)), X]#your are adding bias term it accounts for linear term in data

theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)# used to find optimal weights in linear equation

X_new = np.array([[0], [2], [3]])#contains new data points
X_new_b = np.c_[np.ones((len(X_new), 1)), X_new] #similar to above one just adding bias it gives changed values
y_predict = X_new_b.dot(theta_best)

print("Predictions:", y_predict)
from numpy import loadtxt, zeros, ones, size, array
from sklearn.linear_model import LinearRegression

data = loadtxt(open("machine-learning-ex1/ex1/ex1data1.txt", "rb"), delimiter=',')

y = array(data[:, 1]).T
m = size(y)
X = array([data[:, 0]]).T

regr = LinearRegression(normalize=True)
regr.fit(X, y )

print(regr.intercept_)
print(regr.coef_)
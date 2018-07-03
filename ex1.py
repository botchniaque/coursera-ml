#!/usr/bin/env python2

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import loadtxt, eye, size, ones, zeros, add, multiply, subtract, power, linspace, array, logspace, arange, \
    meshgrid


def warmUpExcersize():
    print(eye(5))


def plotData(x, y):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(X, y, 'rx', MarkerSize=10)
    ax1.set_ylabel('Profit in $10,000s')
    ax1.set_xlabel('Population of City in 10,000s')
    plt.show()


def computeCost(X, y, theta):
    m = size(y)
    J = power(subtract(multiply(theta, X).sum(axis=1), y), 2).sum(axis=0) / (2 * m)
    return J


def gradientDescent(x, y, theta, alpha, num_iters):
    m = size(y)
    J_history = zeros((num_iters, 1))
    for iter in range(num_iters):
        multiply__sum = multiply(theta, x).sum(axis=1)
        x1 = subtract(multiply__sum, y)
        multiply2 = x1.dot(x)
        multiply3 = multiply(multiply2, (alpha / m))
        theta = theta - multiply3
        J_history[iter] = computeCost(x, y, theta)
    return theta, J_history

def plot2(X, y, theta):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(X[:, 1], X.dot(theta), '-')
    ax1.plot(X[:, 1], y, 'rx', MarkerSize=10)
    ax1.set_ylabel('Profit in $10,000s')
    ax1.set_xlabel('Population of City in 10,000s')
    plt.show()

# warmUpExcersize()
data = loadtxt(open("machine-learning-ex1/ex1/ex1data1.txt", "rb"), delimiter=',')

X = data[:, 0]
y = data[:, 1]

m = size(y)

# plotData(X, y)

X = zeros((m, 2))
X[:, :-1] = ones((m, 1))
X[:, 1] = data[:, 0]
theta = zeros(2)

print('Cost for theta %s: %s' % (theta, computeCost(X, y, theta)))
print('Cost for theta %s: %s' % ([-1, 2], computeCost(X, y, [-1, 2])))

iterations = 1500
alpha = 0.01

J = computeCost(X, y, theta)

theta, history = gradientDescent(X, y, theta, alpha, iterations)

print('Theta after fit: %s' % theta)

plot2(X, y, theta)

theta0_vals = linspace(-10, 10, 100)
theta1_vals = linspace(-1, 4, 100)

J_vals = zeros((size(theta0_vals), size(theta1_vals)))

for i in range(0, size(theta0_vals)):
    for j in range(0, size(theta1_vals)):
        t = array([theta0_vals[j], theta1_vals[i]])
        J_vals[i, j] = computeCost(X, y, t.T)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta0_vals, theta1_vals, J_vals, cmap=cm.viridis, shade=True)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
ax.plot(theta[0], theta[1], 'rx')
plt.show()


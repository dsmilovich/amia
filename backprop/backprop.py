#!/usr/bin/python3

import numpy as np

def sigm(x):
    return 1 / (1 + np.exp(-x))
    
def dsigm(x):
    return sigm(x) * (1 - sigm(x))
    
def J(yhat, y):
    return 0.5 * (yhat - y)**2
    
def dy2(yhat, y):
    return yhat - y

x = np.array([1.8, -3.4]).T
y = 5

w1 = np.array([[0.1, -0.5], [-0.3, -0.9], [0.8, 0.02]])
b1 = np.array([0.1, 0.5, 0.8]).T
z1 = w1 @ x + b1
y1 = sigm(z1)

print("z1 =", z1, "y1 =", y1)

w2 = np.array([-0.4, 0.2, -0.5])
b2 = 0.7
z2 = w2 @ y1 + b2
y2 = sigm(z2)

print("z2 =", z2, "y2 =", y2)

dw2 = dy2(y2, y) * dsigm(z2) * y1
print("dw2 =", dw2)

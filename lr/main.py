import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
path  ='LogiReg_data.txt'
pdData = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
pdData.head()
#print dpData.shape
positive = pdData[pdData['Admitted'] == 1]
negative = pdData[pdData['Admitted'] == 0]
fig, ax = plt.subplots(figsize=(10,5))
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=30, c='b', marker='o', label='Admitted')
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=30, c='r', marker='x', label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')
pdData.insert(0,"ones",1)
theta = np.zeros([1,3])
orig_data = pdData.as_matrix()
cols = orig_data.shape[1]
X = orig_data[:,0:cols-1]
Y = orig_data[:,cols-1:cols]
def sigmoid(z):
    return 1/(1+np.exp(-z))

def model(X,theta):
    return sigmoid(np.dot(X,theta.T))

def cost(X,y,theta):
    left = np.multiply(-y,np.log(model(X,theta)))
    right = np.multiply(1 - y,np.log(1 - model(X,theta)))
    return np.sum(left - right) / (len(X))


def gradient(X, y, theta):
    grad = np.zeros(theta.shape)
    error = (model(X, theta) - y).ravel()
    for j in range(len(theta.ravel())):
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)
    return grad
if __name__ == "__main__":
    # print pdData.head(10)
    # print pdData.shape
    # nums = np.arange(-10, 10, step=0.01)
    # fig, ax = plt.subplots(figsize=(12, 4))
    # ax.plot(nums, sigmoid(nums), 'r')
    # plt.show()
    # print cols
    # print orig_data.shape
    # print X[:5]
    # print theta.T
    print X[:,2]
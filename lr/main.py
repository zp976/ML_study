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

def sigmoid(z):
    return 1/(1+np.exp(-z))

def model(X,theta):
    return sigmoid(np.dot)
if __name__=="__main__":
    # nums = np.arange(-10, 10, step=1)  # creates a vector containing 20 equally spaced values from -10 to 10
    # fig, ax = plt.subplots(figsize=(12, 4))
    # ax.plot(nums, sigmoid(nums), 'r')
    plt.show()












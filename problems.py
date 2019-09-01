num = '1,242'
num.replace(",", '')


nums = ['1,242', '1,112', '1,348']

new_nums = []
for num in nums:
    num = int(num.replace(",", ""))
    new_nums.append(num)

print(new_nums)

# List Comprehensions

nums = [int(num.replace(",", "")) for num in nums]
nums


sim_nums = [i+1 for i in range(100)]

# Dictionary Comprehensions

saved_results = {"{}".format(i+1):20*j for i,j in enumerate(sim_nums)}

saved_results['99']

x = list(saved_results.keys())
y = list(saved_results.values())


points = list(zip(x,y))

() # tuple
[] # lists
{[]} # set
{i:j} # dictionary

nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
nums = set(nums)
nums = list(nums)
nums

x_nums = [1,2,3]
y_nums = [4,5,6]

points = set(zip(x_nums, y_nums))
points

# Numpy

## For Loop Version

s = 5

myList = [1,2,3,4,5, 6]

newList = []
for i in myList:
    i = s*i
    newList.append(i)
print(newList)


import numpy as np
myList = np.array(myList)
myList = s * myList
myList

# Average

def mean(x):
    return sum(x) / len(x)

mean(newList)

myList.mean()

myList.std()

np.median(myList)


matrix1 = np.arange(1,4).reshape(1, -1).T
matrix2 = np.arange(4,7).reshape(1, -1)

matrix1.shape
matrix2.shape

np.dot(matrix1.T, matrix2.T)


# Pandas

fruits = {'apples': 5, 'oranges': 7, 'bananas': 10}

fruits['apples']


jim = {'five hour energies': 10, 'hasbro gummy bears': 3, 'frozen section pizza Digiorno': 2}

import pandas as pd

jim_report = pd.DataFrame(jim, index=[0])
t_jim_report = jim_report.T
t_jim_report.columns = ['Quantity']
t_jim_report['price'] = np.array([2.50, 1.25, 7.00])
t_jim_report['subtotals'] = t_jim_report['Quantity'] * t_jim_report['price']
t_jim_report['subtotals'].sum()
t_jim_report.to_excel("jim_shopping.xlsx")

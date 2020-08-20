### Hourglass shape in an array
 # 
### 

# go through entire array to return the highest summed up value of an hourglass


# %%import math
import os
import random
import re
import sys

# %%
# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum = []
    for i in range(len(arr)-2):
        print('i')
        for j in range(len(arr)-2):
            print(j)
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            #         ######top########################******middle****#############bottom####################
    return (max(sum))

# %%
arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

hourglassSum(arr)

# %%

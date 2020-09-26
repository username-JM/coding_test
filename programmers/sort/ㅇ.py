"""
Algorithm
assignment #1
KwangWoon Univ.
2016722065
KIM JUN MO
"""


import time as tt
import random as rr
import matplotlib.pylab as plt
import math


"""
function name : merge_sort
input         : list to sort
output        : sorted list
"""


def merge_sort(x):                        # x is a list to be sorted
    if len(x) > 1:                        # if the length of x is bigger than 1
        left = x[:math.ceil(len(x)/2)]              # separate the x to two lists. the left one is 'left'
        right = x[math.ceil(len(x)/2):]             # the right one is 'right'
        left = merge_sort(left)           # sort left recursively
        right = merge_sort(right)         # sort right recursively
        return merge(left, right)         # return a list which is merged by left and right lists
    return x                              # return x if length of x is 1


"""
function name : merge
input         : two lists to merge
output        : merged list
"""


def merge(x, y):                           # x is a left list, y is a right list
    temp = []                              # temp is a list to save merged list

    while len(x) > 0 and len(y) > 0:       # repeat until one of the lists' length is 0
        if x[0] >= y[0]:                   # if x[0] is equal or bigger than y[0]
            temp.append(y[0])              # add y[0] to temp list
            del y[0]                       # then delete the value from the y list
        else:
            temp.append(x[0])              # add x[0] to temp list
            del x[0]                       # then delete the value from the x list
        # print(temp)
    if len(x) > 0:                         # list y is done. Only list x remains
        while len(x) > 0:                  # repeat until there is no value in x
            temp.append(x[0])              # add x[0] to temp list
            del x[0]                       # delete the value
    elif len(y) > 0:                       # list x is done. Only list y remains
        while len(y) > 0:                  # repeat until there is no value in y
            temp.append(y[0])              # add y[0] to temp list
            del y[0]                       # delete the value

    # print(temp)
    return temp                            # return the merged list 'temp'


"""
function name : make_worst_case
input         : reverse sorted list
output        : worst case list for merge sort
"""


def make_worst_case(x):
    left = []
    right = []
    if len(x) == 1:                     # if the length of the input list 'x' is 1
        return x                        # just return the input list
    while len(x) > 0:                   # if not
        left.append(x[0])               # append it to the left
        del x[0]                        # delete the appended data
        if len(x) == 0:                 # if list is empty
            break                       # break the loop
        right.append(x[0])              # then append it to the right
        del x[0]                        # delete the appended data
    left = make_worst_case(left)        # make worst case recursively
    right = make_worst_case(right)
    return left + right                 # return the worst case list


# now show the simulation results for each case


x = []
for i in range(1, 5001):
    x.append(i)             # sorted list 1 ~ 5000

best_start_time = tt.time()
merge_sort(x)
best_start_time = tt.time() - best_start_time
print("Best case of merge sort : ", end='')     # get best case time
print(best_start_time)

rr.shuffle(x)
avg_start_time = tt.time()
x = merge_sort(x)
avg_start_time = tt.time() - avg_start_time
print('Average case of merge sort : ', end='')      # get avg case time
print(avg_start_time)

x.reverse()
x = make_worst_case(x)                          # make worst case
worst_start_time = tt.time()
merge_sort(x)
worst_start_time = tt.time() - worst_start_time  # get worst case time
print('Worst case of merge sort : ', end='')
print(worst_start_time)

plt.title("Merge Sort : best, average, worst case")
plt.bar([1, 2, 3], [best_start_time, avg_start_time, worst_start_time])  # make graph
plt.show()  # show graph


# now for the various values of n,
# show the graphs of running times for simulations


x_data = [4000, 8000, 12000, 16000, 20000, 24000, 28000, 32000, 36000, 40000]
y_data_worst = []
y_data_best = []
y_data_avg = []
for i in range(0, 10):
    num = x_data[i]
    temp = []
    for j in range(0, num):
        temp.append(num - j)            # get reverse sorted list
    temp = make_worst_case(temp)
    start_time = tt.time()
    temp = merge_sort(temp)
    y_data_worst.append(tt.time() - start_time)     # get worst case time

    start_time = tt.time()
    merge_sort(temp)
    y_data_best.append(tt.time() - start_time)      # get best case time

    rr.shuffle(temp)
    start_time = tt.time()
    merge_sort(temp)
    y_data_avg.append(tt.time() - start_time)       # get avg case time

plt.title("Merge Sort")
plt.plot(x_data, y_data_best, 'r', label='best case')
plt.plot(x_data, y_data_avg, 'g', label='average case')
plt.plot(x_data, y_data_worst, 'b', label='worst case')
plt.legend(loc='upper left')                        # show legend
plt.show()                                          # show graphs


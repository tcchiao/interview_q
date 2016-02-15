'''
Given a list of n integers,
with each integer in the list says you can move up up to that many items in list forward
Returns if you can go from start of list to the end
'''

import sys

def method1(lst):
    goal = len(lst)
    for i in range(len(lst),0,-1):
        if lst[i-1] + i-1 >= goal:
            goal = i-1
    return goal == 0

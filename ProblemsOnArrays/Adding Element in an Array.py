'''
Adding Element in an Array

Problem Statement: Given an array of N integers, write a program to add an array element at the beginning, end, and at a specific pition.

Example:
Input: N = 5, array[] = {1,2,3,4,5}
insertbeginning(6)
insertending(7)
insertatp(8,4)
Output: 6,1,2,8,3,4,5,7
Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at pition 4
'''


a = [1, 2, 3, 4, 5]
def insertbeginning(e):
    a.insert(0, e)
def insertending(e):
    a.append(e)
def insertatp(e, p):
    if 1<=p<=len(a)+1:
        a.insert(p-1,e)
    else:
        print("Invaid position")
insertbeginning(6)
insertending(7)
insertatp(8, 4)
print(*a)

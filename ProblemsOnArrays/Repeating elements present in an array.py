'''
Problem Statement: Find all the repeating elements present in an array.
Examples:
Example 1:
Input: 
Arr[] = [1,1,2,3,4,4,5,2]
Output:
 1,2,4
Explanation:
 1,2 and 4 are the elements which are occurring more than once.
'''

def repeating(r):
    n = len(a)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j] and a[i] not in result:
                result.append(a[i])
                break
    return result
a = [1,1,2,3,4,4,5,2,3]
print(repeating(a))

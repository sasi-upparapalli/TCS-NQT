a = [8, 7, 1, 6, 5, 9]
n = len(a)
a.sort()
mid = n // 2
print(a[:mid] + a[mid:][::-1])
'''
8 7 1 6 5 9
1 5 6 9 8 7
'''


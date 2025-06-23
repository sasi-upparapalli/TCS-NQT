a = [3, 4, 1, 5, 3, -5]
k = 8
n = len(a)

k = k if (k < n) else k % n

r = []
for i in range(k, n):
    r.append(a[i])
for i in range(k):
    r.append(a[i])

print(r)
'''
[1, 5, 3, -5, 3, 4]
'''

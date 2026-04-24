from bisect import bisect_left

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

prev_k = [0] * (n + 1)
pos = {}

for i in range(1, n + 1):
    x = a[i]
    if x not in pos:
        pos[x] = []

    if len(pos[x]) >= k:
        prev_k[i] = pos[x][-k]
    else:
        prev_k[i] = 0

    pos[x].append(i)

roots = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    roots[i] = roots[i - 1] + [prev_k[i]]
    roots[i].sort()

q = int(input())
last = 0

for _ in range(q):
    x, y = map(int, input().split())

    l = (x + last) % n + 1
    r = (y + last) % n + 1

    if l > r:
        l, r = r, l

    arr = roots[r][:]
    for val in roots[l - 1]:
        arr.remove(val)

    last = bisect_left(sorted(arr), l)
    print(last)

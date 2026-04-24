n = int(input())

L = []
R = []
coords = []

for _ in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
    coords.append(l)
    coords.append(r + 1)

coords = sorted(set(coords))

diff = [0] * len(coords)

for i in range(n):
    l = coords.index(L[i])
    r = coords.index(R[i] + 1)
    diff[l] += 1
    diff[r] -= 1

ans = [0] * (n + 1)

cur = 0
for i in range(len(coords) - 1):
    cur += diff[i]
    length = coords[i + 1] - coords[i]
    ans[cur] += length

print(*ans[1:])

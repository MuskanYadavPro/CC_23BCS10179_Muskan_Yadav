t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    found = [False] * (n + 1)

    for i in range(n):
        s = a[i]
        for j in range(i + 1, n):
            s += a[j]
            if s > n:
                break
            found[s] = True

    count = 0
    for x in a:
        if x <= n and found[x]:
            count += 1

    print(count)

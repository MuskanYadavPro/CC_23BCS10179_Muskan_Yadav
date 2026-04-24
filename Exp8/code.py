n = int(input())

a = []
b = []
S = 0

for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
    S += y

maxA = 100 * 100

dp = [[-1] * (maxA + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n - 1, -1, -1):
        for cap in range(maxA - a[i] + 1):
            if dp[j][cap] == -1:
                continue
            dp[j + 1][cap + a[i]] = max(dp[j + 1][cap + a[i]], dp[j][cap] + b[i])

for k in range(1, n + 1):
    best = 0.0

    for cap in range(maxA + 1):
        if dp[k][cap] == -1:
            continue

        sum_b = dp[k][cap]
        value = min(cap, (S + sum_b) / 2.0)
        best = max(best, value)

    print(f"{best:.10f}", end=" ")

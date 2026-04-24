def maxRunTime(n, batteries):
    total = sum(batteries)

    low = 0
    high = total // n
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        power = sum(min(b, mid) for b in batteries)

        if power >= mid * n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


n = int(input())
m = int(input())
batteries = list(map(int, input().split()))

print(maxRunTime(n, batteries))

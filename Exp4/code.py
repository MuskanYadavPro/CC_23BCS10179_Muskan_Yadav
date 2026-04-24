import math

MOD = 10**9 + 7

def nthMagicalNumber(N, A, B):
    left = min(A, B)
    right = N * left
    lcm_ab = math.lcm(A, B)
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        count = mid // A + mid // B - mid // lcm_ab

        if count < N:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1

    return ans % MOD


N, A, B = map(int, input().split())
print(nthMagicalNumber(N, A, B))

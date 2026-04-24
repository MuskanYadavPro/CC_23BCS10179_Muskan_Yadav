n = int(input())
tokens = input().split()

i = 0

def build():
    global i
    if i >= len(tokens):
        return None

    if tokens[i] == "pair":
        i += 1
        left = build()
        right = build()
        if left is None or right is None:
            return None
        return f"pair<{left},{right}>"
    else:
        i += 1
        return "int"

ans = build()

if ans is None or i != n:
    print("Error occurred")
else:
    print(ans)

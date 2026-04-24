class Trie:
    def __init__(self):
        self.end = False
        self.next = [None] * 3


root = Trie()


def insert(word):
    node = root
    for ch in word:
        idx = ord(ch) - ord('a')
        if node.next[idx] is None:
            node.next[idx] = Trie()
        node = node.next[idx]
    node.end = True


def find(node, pos, diff, s):
    if diff > 1:
        return False

    if pos == len(s):
        return diff == 1 and node.end

    cur = ord(s[pos]) - ord('a')

    for i in range(3):
        if node.next[i]:
            if find(node.next[i], pos + 1, diff + (cur != i), s):
                return True

    return False


n, m = map(int, input().split())

for _ in range(n):
    insert(input().strip())

for _ in range(m):
    s = input().strip()
    print("YES" if find(root, 0, 0, s) else "NO")

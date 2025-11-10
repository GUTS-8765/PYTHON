from itertools import filterfalse
i = lambda x: x // 2 - 2
lo, hi = map(int, input().split())
COMP = [False] * i(hi+1)
def cross(p):
    global COMP
    for j in range(i(p * p), len(COMP), p): COMP[j] = True
def iscomposite(c):
    return (c & -2) != 2 and (c < 2 or (c & 1) == 0 or COMP[i(c)])
cross(3)
p, s = 5, 2
while p * p <= hi:
    if not COMP[i(p)]: cross(p)
    p, s = p + s, s ^ 6
print(*filterfalse(iscomposite, range(lo|1, hi+1, 2)))
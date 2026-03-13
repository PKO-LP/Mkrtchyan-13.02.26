def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1

x = float(input())
y = float(input())

print("YES" if IsPointInSquare(x, y) else "NO")
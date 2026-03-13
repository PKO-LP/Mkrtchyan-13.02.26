n = int(input())
arr = list(map(int, input().split()))
result = []
for i in range(1, n):
    if arr[i] > arr[i-1]:
        result.append(arr[i])
print(*result)

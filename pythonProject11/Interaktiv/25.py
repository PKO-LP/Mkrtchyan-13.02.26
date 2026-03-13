n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
        print(min(arr[i-1], arr[i]), max(arr[i-1], arr[i]))
        break
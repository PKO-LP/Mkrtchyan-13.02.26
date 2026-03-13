a = int(input())
b = int(input())
n = int(input())

total_kopecks = (a * 100 + b) * n
rubles = total_kopecks // 100
kopecks = total_kopecks % 100

print(rubles, kopecks)
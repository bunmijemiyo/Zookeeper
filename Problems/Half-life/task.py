N = int(input())
R = int(input())
counter = 0
while N >= R:
    N = N / 2
    counter += 1
print(counter * 12)
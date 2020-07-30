N = int(input())
interest_rate = 0.071
year = 0
while N <= 700000:
    N = (N * interest_rate) + N
    year += 1
print(year)
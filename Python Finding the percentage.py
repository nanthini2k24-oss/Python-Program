n = int(input())
d = {}

for i in range(n):
    x = input().split()

    name = x[0]
    marks = [float(x[1]), float(x[2]), float(x[3])]

    d[name] = marks

name = input()

total = d[name][0] + d[name][1] + d[name][2]
avg = total / 3

print("%.2f" % avg)

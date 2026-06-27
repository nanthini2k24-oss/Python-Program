n = []

for i in range(int(input())):
    x = input().split()

    if x[0] == "insert":
        n.insert(int(x[1]), int(x[2]))

    elif x[0] == "print":
        print(n)

    elif x[0] == "remove":
        n.remove(int(x[1]))

    elif x[0] == "append":
        n.append(int(x[1]))

    elif x[0] == "sort":
        n.sort()

    elif x[0] == "pop":
        n.pop()

    elif x[0] == "reverse":
        n.reverse()

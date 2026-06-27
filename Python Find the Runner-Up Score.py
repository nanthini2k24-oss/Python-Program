n = int(input())
A = list(map(int, input().split()))

mx = max(A)

while mx in A:
    A.remove(mx)

print(max(A))

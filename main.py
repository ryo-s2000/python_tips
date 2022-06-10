# input
N,K=map(int,input().split())
values=list(map(int,input().split()))

# range and index
for index in range(len(values)):
    value = values[index]
    print(index, value)

# enumerate
for index, value in enumerate(values):
    print(index, value)

# for loops
for a1 in range(0, len(A)):
    for a2 in range(a1+1, len(A)):
        for a3 in range(a2+1, len(A)):
            print(a1,a2,a3)

# zip
for n, k in zip(N, K):
    print(n,k)

# enumerate
r = {}
max_key = max(r, key=r.get)

# enumerate
r = []
max_key = max(r, key=r.count)

# bit
l = []
for bit in range(1 << len(l)):
    tmp = 0
    for i in range(len(l)):
        if (bit & (1 << i)):
            tmp += l[i]
       
# unique
l = set(l)

# palindrome
string == string[::-1]

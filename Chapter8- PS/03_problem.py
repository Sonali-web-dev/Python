'''
s(1) = 1
s(2) = 2
s(3) = 3
s(n) = 1+2+3+4....n
s(n) = s(n-1) + n
'''
def sum(n):
    if (n==1):
        return 1
    return sum(n-1) + n

print(sum(9))

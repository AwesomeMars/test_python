# 반복적으로 풀기

def fibo(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b

    return b


for n in range(1, 11):
    print(n, fibo(n))

# while 문 버전
N = int(input())

0 <= N <= 20

factorial = 1

if N == 0:
    print(1)

else:
    i = N
    while i > 0:
        factorial *= i
        i -= 1

    print(factorial)

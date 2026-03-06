# for 문
N = int(input())

0 <= N <= 20

factorial = 1

if N == 0:
    print(1)

else:
    for i in range(1, N+1):
        factorial *= i

    print(factorial)
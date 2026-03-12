# 피보나치 수 5 - bronze 2
# 수학, 구현

'''
피보나치 수열
0번째 = 0
1번째 = 1
n번째 = (n-1)번째 + (n-2)번째 - 재귀
'''

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

n = int(input())
result = fibonacci(n)
print(result)
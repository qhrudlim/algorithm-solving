# 팩토리얼 0의 개수 - silver 5
# 수학

'''
10의 개수 = 2 x 5의 개수 = 5의 개수
(팩토리얼에서 2는 항상 5보다 많으므로 5의 개수가 곧 10의 개수)
=> 기존 수를 5로 나눈 몫을 새로운 수로 갱신하며 계속 더하기
'''

def count_zeros(num):
    if num == 0:
        return 0
    
    cnt = 0
    while num > 0:
        num //= 5
        cnt += num
    return cnt

N = int(input())
result = count_zeros(N)
print(result)
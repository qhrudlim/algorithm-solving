# 회사에 있는 사람 - silver 5
# 자료구조, 해시를 사용한 집합과 맵

'''
출입 기록 = 이름 enter/leave
enter = 출근
leave = 퇴근
동명이인 미존재, 대소문자가 다르면 다른 사람
'''

'''
list는 시간초과 - O(n^2)
set으로 변경 - O(log n)
=> 시간복잡도 감소
'''

n = int(input())

curr_employee = set()
for _ in range(n):
    name, commute = input().split()

    if commute == 'enter':
        curr_employee.add(name)
    elif commute == 'leave':
        curr_employee.discard(name)

result = sorted(curr_employee, reverse=True)
print(*result, sep='\n')
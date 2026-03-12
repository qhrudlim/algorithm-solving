import sys
sys.stdin = open('study/0808/22375/switch_sample_in.txt')

'''
T: 테스트 케이스 수
N: 스위치 개수
A: 조작 전 스위치 상태
B: 조작 후 스위치 상태

i번 스위치 조작 시 i ~ N번 스위치 상태 변경
ex) 0 0 0 -> 0 1 0
첫번째: 2번 스위치 - 0 1 1
두번쨰: 3번 스위치 - 0 1 0
총 두번 필요

0 1 1 0 0 -> 0 0 0 1 1
2번 - 0 1 1 0 0 -> 0 0 0 1 1
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A, B = [list(map(int, input().split())) for _ in range(2)]

    diff = [a ^ b for a, b in zip(A, B)]
    switch_cnt = sum(a != b for a, b in zip([0] + diff, diff))

    print(f'#{tc}', switch_cnt)
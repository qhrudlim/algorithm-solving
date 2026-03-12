import sys
sys.stdin = open('sample_in.txt')

'''
NxN 격자에서 행의 합 + 열의 합 - 현재 셀 값의 최댓값 찾기
T: 테스트 케이스 수
N: 격자의 크기
arr: NxN 격자 배열
row_sums: 각 행의 합을 담은 리스트
col_sums: 각 열의 합을 담은 리스트
max_score: 최대 점수

모든 행과 열의 합을 미리 계산한 후 각 셀에서 조회하여 시간복잡도 줄이기
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    row_sums = [sum(arr[row]) for row in range(N)]
    col_sums = [sum(arr[row][col] for row in range(N)) for col in range(N)]

    max_score = max(row_sums[r] + col_sums[c] - arr[r][c] for r in range(N) for c in range(N))

    print(f'#{tc}', max_score)
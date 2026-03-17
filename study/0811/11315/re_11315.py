import sys
sys.stdin = open('study/0811/11315/sample_input.txt')

'''
NxN 보드에서 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯개 이상 연속한 부분이 있는지 판정

o: 돌이 있는 칸
.: 돌이 없는 칸

다섯개 이상 연속한 부분이 있으면 YES, 없으면 NO 출력

보드의 크기만큼 반복하며,
현재 칸이 'o'이면 4가지 방향(가로, 세로, 우하향, 좌하향)으로 4칸 앞까지 탐색하여
연속된 'o'의 개수 세기
-> 5개 이상이면 YES, 아니면 NO 반환
'''

dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1]

def find_five():
    words = "NO"
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for d in range(4):
                    cnt = 1
                    for k in range(1, 5):
                        nr, nc = r + dr[d] * k, c + dc[d] * k
                        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 'o':
                            break
                        cnt += 1
                    if cnt >= 5:
                        words = "YES"
                        return words
    return words


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = find_five()
    print(f'#{tc}', result)
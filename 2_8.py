def max_blocks(n, blocks):
    # 각 방향에서 볼 수 있는 최대 높이를 계산
    max_north_south = [max(blocks[i][j] for i in range(n)) for j in range(n)]  # 남북 방향에서 볼 수 있는 최대 높이
    max_east_west = [max(blocks[i]) for i in range(n)]  # 동서 방향에서 볼 수 있는 최대 높이

    # 각 위치에서 쌓을 수 있는 최대 블록 수를 계산
    total = 0
    for i in range(n):
        for j in range(n):
            # 각 방향에서 볼 수 있는 최대 높이 중 작은 값과 현재 블록의 높이 사이의 차이를 더함
            total += min(max_north_south[j], max_east_west[i]) - blocks[i][j]

    return total  # 총 블록 수를 반환

# 사용자 입력 받기
n = int(input("받침대의 크기를 입력하세요: "))  # 받침대의 크기를 입력받음
blocks = []  # 블록의 높이를 저장할 리스트
for _ in range(n):  # 각 줄에 대해
    row = list(map(int, input("블록의 높이를 입력하세요: ").split()))  # 블록의 높이를 입력받음
    blocks.append(row)  # 블록의 높이를 리스트에 추가

print(max_blocks(n, blocks))  # 총 블록 수를 출력


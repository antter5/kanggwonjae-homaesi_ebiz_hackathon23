# collections 모듈에서 deque 클래스를 가져온다.
from collections import deque  

# 행렬에서 최단 경로를 찾기 위한 함수(shortest_route)를 정의
def shortest_route(matrix, target):
    if not matrix or not matrix[0]:
        return None

    # 행렬의 행과 열 각각 개수 찾기
    rows, cols = len(matrix), len(matrix[0])

    # 방문한 셀을 추적하기 위한 2차원 불린(T/F) 배열을 생성
    visited = [[False] * cols for _ in range(rows)]

    # 셀이 유효하고 처음 방문하는지 확인하는 함수(is_valid) 만들기
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y]

    # 가능한 이동 방향을 정의(한칸 기준): 오른쪽, 아래, 왼쪽, 위
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 시작 셀 (1, 1)과 빈 경로를 가지고 큐를 초기화
    queue = deque([(1, 1, [])])

    # 너비 우선 탐색 (BFS) 수행
    while queue:
        x, y, path = queue.popleft()  # 현재 셀과 경로를 얻기

        visited[x][y] = True  # 현재 셀을 방문한 것으로 표시

        # 현재 셀이 목표 값을 포함하는지 확인하기
        if matrix[x][y] == target:
            return path + [(x, y)]  # 목표 셀과 현재 셀이 일치할 때 위치 return

        # 모든 방향에서 이웃 셀을 탐색하기 
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy  # 새로운 셀 좌표를 계산

            if is_valid(new_x, new_y):  # 새로운 셀이 유효한지 확인하기
                new_path = path + [(x, y)]  # 경로를 확장하기
                queue.append((new_x, new_y, new_path))  # 새로운 셀을 큐에 추가하기

    return None  # 목표로 가는 경로를 찾지 못한 경우 None을 리턴

# 1부터 36까지의 요소가 있는 6x6 행렬을 생성합니다.
matrix = [[i + j * 6 + 1 for i in range(6)] for j in range(6)]

N = 12  # 1부터 36 중 원하는 값 입력 ex)12

result = shortest_route(matrix, N)  # 목표에 대한 최단 경로를 찾기

if result:
    sum_of_movements = len(result) - 1  # 이동 횟수의 합을 계산 (시작 셀을 제외하므로 -1)
    print(f"최소 이동 횟수: {sum_of_movements}")  # 이동 횟수를 출력
else:
    print("경로를 찾을 수 없습니다.")  # 경로를 찾지 못한 경우 출력할 메시지.

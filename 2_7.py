def min_moves():
    # 사용자로부터 N을 입력받음
    N = int(input("정수 N을 입력하세요: "))

    # N의 약수를 찾음
    i = 1
    moves = N
    while i * i <= N:
        if N % i == 0:
            j = N // i
            moves = min(moves, i + j - 2)
        i += 1

    return moves

# 함수 호출
print(min_moves())

# 2위 1오
# 1위 2오
# 1아 2오
# 2아 1오
# 어떻게 하든 겹치진 않음..
# 즉 어떻게든 쟤네 경우의 수를 우겨넣는게 중요
# 오른쪽으로만 가기때문에 오른쪽으로 한칸 가면 가장 왼쪽 한 줄을 빼야됨

# 세로100 가로50 50 * 100
# 가로가 더 크면 1위2오 1아2오 우선 세로가 더 크면 2위1오 2아1오 우선
# 세로가 더 크다 -> 2위1오 2아1오

# 처음 1줄 없앰, 1칸 방문
# 2위 1오 -> 한줄 없앰 49 1칸 추가
# 2아 1오 -> 한줄 없앰 48 1칸 추가
# 1위 2오 -> 두줄 없앰 46 1칸 추가
# 1아 2오 -> 두줄 없앰 44 1칸 추가
# 6줄 없어짐! , 4칸 방문
# 남은 43줄은 2위 1오 2아 1오에 몰빵 -> 43칸 방문
# 줄 0 끝
# 합 48

# 세로 1 가로 1
# 가로 세로 똑같다 -> 1위2오 1아2오
# 처음 1줄 없앰, 1칸 방문
# 줄 0 끝
# 합 1

# 세로 17 가로 5
# 세로가 더 크다 -> 2위1오 2아1오

# 처음 1줄 없앰, 1칸 방문
# 2위 1오 -> 한줄 없앰 49 1칸 추가
# 2아 1오 -> 한줄 없앰 48 1칸 추가
# 1위 2오 -> 두줄 없앰 46 1칸 추가
# 줄 0 끝
# 합 4


# `
# 0 `
#   `
# ` 0
# `
# 0

# 세로 가로
n, m = map(int, input().split())
5
i = 1
cnt = 0

if n == 1 or m == 1:
    cnt += 1

elif n == 2:
    if m < 3:
        cnt += 1
    elif m < 5:
        cnt += 2
    elif m < 7:
        cnt += 3
    else:
        cnt += 4
else:
    if m < 7:
        if m < 4:
            cnt += m
        else:
            cnt += 4
    else:
        cnt += (m - 2)

print(cnt)

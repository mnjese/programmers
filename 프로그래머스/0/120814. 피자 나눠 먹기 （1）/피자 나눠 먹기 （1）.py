def solution(n):
    answer = 1
    cnt = n
    while (cnt > 7):
        cnt -= 7
        answer += 1
    return answer
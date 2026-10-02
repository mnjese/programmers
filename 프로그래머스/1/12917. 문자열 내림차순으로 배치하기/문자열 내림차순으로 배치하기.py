def solution(s):
    chars = sorted(s, reverse=True)
    answer = ''
    for i in chars:
        answer += i
    return answer
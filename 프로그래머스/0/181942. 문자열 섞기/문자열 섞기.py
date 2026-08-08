def solution(str1, str2):
    answer = ''
    m = 0
    for i in range(len(str1)):
        answer += str1[m]
        answer += str2[m]
        m += 1
    return answer
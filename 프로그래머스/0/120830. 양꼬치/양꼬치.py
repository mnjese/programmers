def solution(n, k):
    answer = 0
    s = n//10
    k -= s
    answer = n*12000 + k*2000
    return answer
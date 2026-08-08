def solution(number, n, m):
    answer = 0
    if (n>=m) and (n%m==0):
        gcd = n
    elif (n<m) and (m%n==0):
        gcd = m
    else:
        gcd = n*m

    if (number%(gcd) == 0):
        answer = 1
    return answer
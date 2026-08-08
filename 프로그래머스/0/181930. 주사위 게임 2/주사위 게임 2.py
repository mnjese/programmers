def solution(a, b, c):
    answer = 0
    sum1 = a+b+c
    sum2 = a*a+b*b+c*c
    sum3 = a*a*a+b*b*b+c*c*c
    if (a==b and b==c and a==c):
        answer = sum1*sum2*sum3
    elif (a!=b and b!=c and a!=c):
        answer = sum1
    else:
        answer = sum1*sum2
    return answer
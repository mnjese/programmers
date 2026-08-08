def solution(a, b):
    answer = 0
    aa = ''
    bb = ''
    aa += str(a)
    bb += str(b)
    if int(aa+bb) >= 2*a*b:
        answer = int(aa+bb)
    else:
        answer = 2*a*b
    return answer
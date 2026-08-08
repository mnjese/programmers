def solution(a, b):
    answer = ''
    aa = ''
    bb = ''
    aa += str(a)
    bb += str(b)
    if int(aa + bb) >= int (bb + aa):
        answer = int(aa+bb)
    else:
        answer = int(bb+aa)
    answer = int(answer)
    return answer
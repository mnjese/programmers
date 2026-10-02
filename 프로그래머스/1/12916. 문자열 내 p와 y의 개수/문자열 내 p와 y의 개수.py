def solution(s):
    s = s.lower() 
    c1 = 0
    c2 = 0
    for i in s:
        if i == "p":
            c1 += 1
        if i == "y":
            c2 += 1
    if c1 == c2:
        return True
    else:
        return False
    return True
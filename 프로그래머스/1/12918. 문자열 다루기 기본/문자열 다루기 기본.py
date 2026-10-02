def solution(s):
    
    check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(s) != 4 and len(s) != 6:
        return False
    for i in s:
        answer = False
        for j in check:
            if i == j:
                answer = True
        if answer == False:
            return False
    return True
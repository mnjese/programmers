def solution(code):
    answer = ''
    mode = 0
    idx = 0
    for i in code:
        if mode == 0:
            if (code[idx] != "1"):
                if (idx%2 == 0):
                    answer += i
            else:
                mode = 1       
        else:
            if (code[idx] != "1"):
                if (idx%2 == 1):
                    answer += i
            else:
                mode = 0
        idx += 1
    if (len(answer) == 0):
        answer ="EMPTY"
    return answer
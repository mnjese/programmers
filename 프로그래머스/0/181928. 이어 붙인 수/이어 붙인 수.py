def solution(num_list):
    answer = 0
    result1 = ''
    result2 = ''
    
    for i in num_list:
        if (i%2 == 1):
            result1 += str(i)
        else:
            result2 += str(i)
            
    answer = int(result1) + int(result2)
    return answer
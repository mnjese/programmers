def solution(array):
    answer = [0,0]
    cnt = -1
    max1 = 0
    for i in range(len(array)):
        if (array[i] > max1):
            max1 = array[i]
            cnt = i
    answer[0] = max1
    answer[1] = cnt
    return answer
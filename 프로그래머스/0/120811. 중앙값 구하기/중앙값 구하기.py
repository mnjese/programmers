def solution(array):
    answer = 0
    array.sort()
    for i in range(len(array)//2+1):
        answer = array[i]
    return answer
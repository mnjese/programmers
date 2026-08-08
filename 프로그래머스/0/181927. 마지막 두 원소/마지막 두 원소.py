def solution(num_list):
    answer = []
    for i in num_list:
        answer.append(i)
    max1 = 0
    cnt = len(num_list)
    if(num_list[cnt-1] > num_list[cnt-2]):
        answer.append(num_list[cnt-1] - num_list[cnt-2])
    else:
        answer.append(num_list[cnt-1]*2)
    return answer
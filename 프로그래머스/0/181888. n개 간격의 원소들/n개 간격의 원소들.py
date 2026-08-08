def solution(num_list, n):
    answer = []
    for i in num_list:
        answer = num_list[::n]
    return answer
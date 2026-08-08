def solution(num_list):
    answer = 0
    cnt1 = 1
    cnt2 = 0
    for i in num_list:
        cnt1 *= i
        cnt2 += i
    cnt2 = cnt2*cnt2 
    if (cnt1 < cnt2):
        answer = 1
    else:
        answer = 0
    return answer
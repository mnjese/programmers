def solution(age):
    answer = ''
    apb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    age = str(age)
    
    for i in age:
        answer += apb[int(i)]
        
    return answer
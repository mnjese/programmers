def solution(numbers):
    answer = []
    
    for i in numbers: #i값은 numbers 배열의 첫 번째 값부터 마지막 값까지를 의미, range를 써야 i가 0부터 시작
        answer.append(i*2)
    return answer
def solution(answers):
    number1 = [1, 2, 3, 4, 5]
    number2 = [2, 1, 2, 3, 2, 4, 2, 5]
    number3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i, a in enumerate(answers):
        if (a == number1[i%5]):
            score[0] += 1
        if (a == number2[i%8]):
            score[1] += 1   
        if (a == number3[i%10]):
            score[2] += 1
    return [i + 1 for i in range(3) if score[i] == max(score)]
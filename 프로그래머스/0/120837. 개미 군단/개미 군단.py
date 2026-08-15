def solution(hp):
    m1 = hp//5
    m2 = (hp%5)//3
    m3 = hp-m1*5-m2*3
    answer = m1+m2+m3
    return answer
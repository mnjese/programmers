def solution(sizes):
    big = 0
    small = 0
    for w, h in sizes:
        big = max(big, max(w,h))
        small = max(small, min(w,h))
    return big*small
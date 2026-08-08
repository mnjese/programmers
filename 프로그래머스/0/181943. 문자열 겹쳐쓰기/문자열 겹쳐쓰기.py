def solution(my_string, overwrite_string, s):
    answer = my_string[:s:1]+overwrite_string[::1]+my_string[s+len(overwrite_string)::1]
        
    return answer
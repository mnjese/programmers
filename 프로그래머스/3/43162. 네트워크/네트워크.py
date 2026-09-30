from collections import deque

def solution(n, computers):
    visited = [False]*n
    answer = 0
    
    for start in range(n):
        if visited[start]:
            continue
        answer += 1
        visited[start] = True
        q = deque([start])
        
        while q:
            node = q.popleft()
            for nxt in range(n):
                if computers[node][nxt] == 1 and not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
    return answer

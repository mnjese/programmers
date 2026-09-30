from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dist = [[0]*m for _ in range(n)]
    dist[0][0] = 1
    
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == 0 and maps[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
            
    return dist[n-1][m-1] if dist[n-1][m-1] else -1
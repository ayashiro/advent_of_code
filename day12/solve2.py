import sys, queue, string
with open(sys.argv[1]) as f:
    table = []
    start = (-1,-1)
    goal = (-1,-1)
    for line in f.readlines():
        table.append([])
        for c in line.strip():
            if c in string.ascii_lowercase:
                table[-1].append(ord(c) - ord('a'))
            elif c == 'S':
                start = len(table) - 1 , len(table[-1])
                table[-1].append(0)
            elif c == 'E':
                goal = len(table) - 1 , len(table[-1])
                table[-1].append(25)
    qu = queue.Queue()
    qu.put((goal[0], goal[1], 0))
    visited  =[[1e60 for c in v] for v in table]
    visited[goal[0]][goal[1]] = 0
    DX = [-1,1,0,0]
    DY = [0,0,1,-1]
    while not qu.empty():
        now_x, now_y, now_dist = qu.get()
        for dx, dy in zip(DX, DY):
            next_x, next_y, next_dist = now_x + dx , now_y + dy, now_dist + 1
            if  next_x < len(table) and next_x >= 0 :
                if next_y < len(table[next_x]) and next_y >= 0:
                    if  table[now_x][now_y]  <= table[next_x][next_y] + 1 and next_dist < visited[next_x][next_y]:
                        visited[next_x][next_y] = next_dist
                        qu.put((next_x, next_y, next_dist))
    ans = visited[start[0]][start[1]]
    for a, b  in zip(table, visited):
        for c ,d  in zip(a,b):
            if c == 0:
                ans = min(d, ans)
    print(ans)

    

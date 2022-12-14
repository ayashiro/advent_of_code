import sys 
directions = "RLUD"
dx = (0,0,-1,1)
dy = (1, -1, 0 ,0)
with open(sys.argv[1]) as f:
    hx,hy = 0,0
    tx,ty = 0,0
    tail_visited = set()
    tail_visited.add((tx,ty))
    for line in f.readlines():
        d, step = line.strip().split()
        d = directions.index(d)
        step = int(step)
        for _ in range(step):
            nhx, nhy = hx + dx[d] , hy + dy[d]
            if max(abs(tx  - nhx), abs(ty - nhy)) > 1:
                tx, ty = hx, hy
            hx,hy  = nhx, nhy
            tail_visited.add((tx,ty))
    print(len(tail_visited))

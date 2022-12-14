import sys 
directions = "RLUD"
dx = (0,0,-1,1)
dy = (1, -1, 0 ,0)
with open(sys.argv[1]) as f:
    positions = [(0,0)] * 10
    tail_visited = set()
    tail_visited.add((0,0))
    def printH():
        for i in range(-10, 10):
            t = ""
            for j in range(-10, 10):
                if (i,j) not in positions:
                    t += "."
                else :
                    t += str(positions.index((i,j)))
            print(t.replace("0", "H"))
        print()        
    for line in f.readlines():
        d, step = line.strip().split()
        d = directions.index(d)
        step = int(step)
        for _ in range(step):
            new_positions = []
            hx,hy = positions[0]
            new_positions.append((hx + dx[d] , hy + dy[d]))
            for i in range(1,10):
                px, py = new_positions[i-1]
                nx, ny = positions[i]
                if max(abs(nx-px), abs(ny-py)) > 1 :
                    if min(abs(nx-px), abs(ny-py)) == 0 :
                        if nx - px == 2 :
                            nx -= 1
                        elif px - nx == 2 :
                            nx += 1
                        elif ny - py == 2 :
                            ny -= 1
                        elif  py - ny == 2 :
                            ny += 1
                    else:
                        for ddx,ddy in [(1,1), (-1,1), (1,-1), (-1,-1)]:
                            if max(abs(nx + ddx -px), abs(ny + ddy - py)) <= 1:
                                nx, ny = nx+ddx , ny + ddy
                                break
                new_positions.append((nx,ny))
            positions = new_positions                        
            tail_visited.add(positions[-1])
        printH()
            

    print(len(tail_visited))

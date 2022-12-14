import sys
blocked = set()
rocked = set()
with open(sys.argv[1]) as f :
    lines = [[tuple(map(int,v.strip().split(",")))  for v in line.split("->")] for line in f.readlines()]
    for blocks in lines:
        for s, e in zip(blocks[:-1], blocks[1:]):
            if s[0] == e[0]:
                if s[1] > e[1]:
                    s,e = e,s
                for t in range(s[1], e[1] + 1):
                    blocked.add((s[0], t))
            if s[1] == e[1]:
                if s[0] > e[0]:
                    s,e = e,s
                for t in range(s[0], e[0] + 1 ):
                    blocked.add((t, s[1]))
    def status_print():
        Ys = list(map(lambda x : x[0], blocked.union(rocked)))
        Xs = list(map(lambda x : x[1], blocked.union(rocked)))    
        for x in range(min(Xs + [0]), max(Xs) + 1) :
            tmp = []
            for y in range(min(Ys), max(Ys) + 1 ):
                if (y,x) in blocked:
                    tmp.append("#")
                elif (y,x) in rocked:
                    tmp.append("o")
                else :
                    tmp.append(".")
            print("".join(tmp))
    cnt = 0
    nowx, nowy = -1, -1
    maxy = max(map(lambda x:x[1], blocked)) + 2
    while nowy < maxy:
        nowx, nowy = 500, 0
        dx = (0,-1,1)
        dy = (1, 1, 1)
        while nowy  < maxy:
            proceed = False
            for ddx , ddy in zip(dx, dy):
                nx , ny = nowx + ddx , nowy+ddy
                if (nx, ny) not in blocked and (nx, ny) not in rocked:
                    proceed = True
                    nowx, nowy = nx, ny
                    break
            if not  proceed: break
        rocked.add((nowx, nowy))
        cnt += 1
        #status_print()
    status_print()
    print(cnt - 1 )
        
            
        
                
                    
            
        
        
        

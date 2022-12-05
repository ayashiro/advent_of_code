import re,sys
with open(sys.argv[1]) as f :
    t = f.readlines()
    lines = [line for line in t]
    stacks = []
    for line in lines:
        N = len(line)
        if len(stacks) == 0:
            for _ in range(N//4):
                stacks.append([])
        if "[" in line:
            for i in range(0,N,4):
                if line[i+1] != ' ':
                    stacks[i//4].insert(0,line[i+1])
        if "move" in line:
            _, times, _ ,fr , _, to  =  line.split()
            times, fr, to = int(times),int(fr) -1 , int(to) -1
            print(times,fr,to)
            x = []
            for _ in range(times):
                x.append(stacks[fr].pop())
            for v in x[::-1] :
                stacks[to].append(v)
            #            stacks[to].append(stacks[fr],pop())
            print(stacks)

                    
    print("".join([s[-1] for s in stacks]))



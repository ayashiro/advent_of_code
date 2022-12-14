import sys
with open(sys.argv[1]) as f:
    value = 1
    d = [1]
    for line in f.readlines():
        line = line.strip()
        if line == "noop":
            d += [value]
        else :
            d += [value]*2
            value += int(line.split()[1])
    print(sum(ind * d[ind] for ind in range(20, len(d), 40))) # silver star
    print("".join(("." if abs((i-1) % 40 - d[i]) > 1 else "#") + ("\n" if i%40 == 0 else "")  for i in range(1,len(d))))  #gold star
        


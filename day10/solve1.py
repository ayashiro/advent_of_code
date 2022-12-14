import sys
with open(sys.argv[1]) as f:
    circle = 0
    value = 1
    d = {}
    d[0]=1
    for line in f.readlines():
        line = line.strip()
        if line == "noop":
            circle += 1
            d[circle] = value
        elif line.startswith("addx"):
            _, addx = line.split()
            addx = int(addx)
            circle += 1
            d[circle] = value
            circle += 1
            d[circle]  = value
            value += addx
    ans = 0
    for k,v in d.items():
        if (k - 20 ) % 40 == 0 :
            ans += k * v
    print(ans)
        

import sys
with open(sys.argv[1]) as f:
    for line in f.readlines():
        s = set()
        for i,l in enumerate(line.strip()):
            if len(set(line[i:i+14])) == 14:
                print(line.strip(),i+14)
                break

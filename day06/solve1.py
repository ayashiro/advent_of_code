import sys
with open(sys.argv[1]) as f:
    for line in f.readlines():
        for i,l in enumerate(line.strip()):
            if len(set(line[i:i+4])) == 4:
                print(line.strip(),i+4)
                break

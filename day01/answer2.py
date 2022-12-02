with open("input2.txt") as f :
    print(sum(sorted(sum(map(int , v.split())) for v in f.read().strip().split("\n\n"))[-3:]))

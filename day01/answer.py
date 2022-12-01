with open("input") as f :
    print(max(sum(map(int, v.split())) for v in f.read().strip().split("\n\n")))

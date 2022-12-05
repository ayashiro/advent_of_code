import sys 
with open(sys.argv[1]) as f :
    count = 0 
    for line in f.readlines():
        (a,b), (c,d) =  [[ int(t) for t in x.split("-")] for x in  line.split(",")]
        if len(set(range(a,b+1)) & set(range(c,d+1)))  == min(b-a , d-c ) + 1: 
            count += 1
    print(count)


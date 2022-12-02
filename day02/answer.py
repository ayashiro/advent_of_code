import sys
with open (sys.argv[1]) as u:
    print(sum(p + 1 + 3*((p-c + 1) %3) for c,p in (map(lambda t:'ABCXYZ'.index(t)%3,l.strip().split()) for l in u.readlines())))

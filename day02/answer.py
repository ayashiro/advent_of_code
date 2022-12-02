import sys
with open (sys.argv[1]) as u:
    print(sum(p-3+3*((p-c)%3)for c,p in(map(lambda t:'ABC XYZ'.index(t),l.split()) for l in u.readlines())))

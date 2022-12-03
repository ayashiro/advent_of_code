import sys, string
with open(sys.argv[1]) as f:
    print(sum((' '+string.ascii_lowercase+string.ascii_uppercase).index(list(set(l[:N]).intersection(l[N:]))[0]) for l, N in [(v, len(v)//2) for v in f.readlines()]))

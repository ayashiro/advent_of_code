import sys, string
with open(sys.argv[1]) as f:print(sum((' '+ string.ascii_lowercase + string.ascii_uppercase).index(list(set(a).intersection(set(b)).intersection(set(c)))[0]) + 1 for a,b,c in zip(*(lambda l : (l[::3], l[1::3], l[2::3]))( [v.strip() for v in f.readlines()]))))

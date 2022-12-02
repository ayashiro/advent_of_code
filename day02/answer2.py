import sys
print(sum((p+c-1)%3 + 1 + p%3*3  for c,p in (("ABC YZX".index(t) for t in l.split()) for l in open(sys.argv[1]).readlines())))

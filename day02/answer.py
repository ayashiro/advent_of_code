import sys
with open (sys.argv[1]) as u:print(sum((lambda p,c:[1,2,3][p] + [0,3,6][((p-c) + 1) %3])(*map(lambda t:{"X" : 0 , "Y": 1, "Z" : 2, "A":0, "B":1, "C":2}[t],(b,a))) for a,b in [l.strip().split() for l in u.readlines()]))

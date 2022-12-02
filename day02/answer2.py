import sys
with open (sys.argv[1]) as u:print(sum((lambda p,c:[1,2,3][(p+c)%3] + [0,3,6][(p  + 1) %3])(*map(lambda t:{"X" : 2 , "Y": 0, "Z" : 1, "A":0, "B":1, "C":2}[t],(b,a))) for a,b in [l.strip().split() for l in u.readlines()]))

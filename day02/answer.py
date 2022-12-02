import sys
with open (sys.argv[1]) as f:
    point_for_shape = [1,2,3]
    point_for_result = [0,3,6]
    convert = {"X" : 0 , "Y": 1, "Z" : 2, "A":0, "B":1, "C":2}
    ans = 0
    for a,b in [line.strip().split() for line in f.readlines()]:
        print(a,b)
        player = convert[b]
        computer = convert[a]
        s_p = point_for_shape[player]
        result = point_for_result[(( player - computer) + 1)%3]
        print(f"{s_p} + {result}")
        ans += s_p + result
    print(ans)

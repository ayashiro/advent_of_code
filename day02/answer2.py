import sys
with open (sys.argv[1]) as f:
    point_for_shape = [1,2,3]
    point_for_result = [0,3,6]
    convert_player = {"X" : 2, "Y": 0, "Z":1}
    convert = {"A":0, "B":1, "C":2}
    ans = 0
    for a,b in [line.strip().split() for line in f.readlines()]:
        print(a,b)
        computer = convert[a]
        player = (convert_player[b] + computer) % 3
        s_p = point_for_shape[player]
        result = point_for_result[(( player - computer) + 1)%3]
        print(f"{s_p} + {result}")
        ans += s_p + result
    print(ans)

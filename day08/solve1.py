import sys
def update_visible_horizontal(irange, jrange, visible, table):
    for i in irange:
        max_height = 0
        for j in jrange:
            if table[i][j] > max_height:
                visible[i][j] = True
                max_height  = table[i][j]
def update_visible_vertical(irange, jrange, visible,table):
    for j in jrange:
        max_height = 0
        for i in irange:
            if table[i][j] > max_height:
                visible[i][j] = True
                max_height = table[i][j]

with open(sys.argv[1]) as f:
    table = [[int(l) for l in line.strip()] for line in f.readlines()]
    visible = [[False for _ in t] for t in table ]
    H = len(table)
    W = len(table[0])
    update_visible_horizontal(range(H), range(W), visible, table)
    update_visible_horizontal(range(H), range(W-1, -1, -1), visible, table)
    update_visible_vertical(range(H), range(W), visible, table)
    update_visible_vertical(range(H-1, -1, -1), range(W), visible, table)
    count_invisible = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if not visible[i][j]:
                print(f"{i},{j} is invisible")
                count_invisible += 1
    print(H*W - count_invisible)

import sys
def update_score_horizontal(irange, jrange, score, table, start):
    for i in irange:
        stack = [(start, 100000000)] # (index, max_height)
        for j in jrange:
            print("hor",stack, i, j)
            while stack  and stack[-1][1] < table[i][j]:
                stack.pop()
            if stack : 
                ind = stack[-1][0]
                score[i][j].append(abs(j-ind))
                print("score mul", abs(j-ind))
            stack.append((j, table[i][j]))
def update_score_vertical(irange, jrange, score, table, start):
    for j in jrange:
        max_height = 0
        stack = [(start, 100000)]
        for i in irange:
            print("ver",stack, i, j)            
            while stack  and stack[-1][1] < table[i][j]:
                stack.pop()
            if stack :
                ind = stack[-1][0]
                score[i][j].append(abs(i-ind))
                print("score mul", abs(i-ind))                
            stack.append((i, table[i][j]))

with open(sys.argv[1]) as f:
    table = [[int(l) for l in line.strip()] for line in f.readlines()]
    score = [[[] for _ in t] for t in table]
    H = len(table)
    W = len(table[0])
    update_score_horizontal(range(H), range(W), score, table, 0)
    update_score_horizontal(range(H), range(W-1, -1, -1), score, table, W-1)
    update_score_vertical(range(H), range(W), score, table, 0)
    update_score_vertical(range(H-1, -1, -1), range(W), score, table, H-1)
    max_score = 1
    for i in range(H):
        for j in range(W):

            tmp = 1
            for v in score[i][j]:
                tmp *= v
            print(f"{i},{j} is {score[i][j]}, {tmp}")
            max_score = max(max_score, tmp)
    print(max_score)

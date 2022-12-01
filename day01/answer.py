print(max( sum(tuple(map(int,filter(lambda s :len(s) > 0 ,v.split("\n"))))) for v in "".join( open("input").readlines()).split("\n\n")))

import sys,re
with open(sys.argv[1]) as f:
    max_y = int(sys.argv[2])
    lines = [line.strip() for line in f.readlines()]
    pat = re.compile(r"Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)")
    beacons = set()
    coord = {}
    for index, line in enumerate(lines):
        m = pat.match(line)
        s_x, s_y = int(m.group(1)), int(m.group(2))
        b_x, b_y = int(m.group(3)), int(m.group(4))
        beacons.add((b_x, b_y))
        m_d = abs(s_x - b_x) + abs(s_y  - b_y)
        for ny in range(max(0, s_y - m_d), min(max_y, s_y + m_d) + 1):
            rest_md = m_d - abs(s_y - ny)
            if ny not in coord:
                coord[ny] = []
            coord[ny].append((max(s_x - rest_md, 0), min(s_x + rest_md, max_y) ))
    #print(coord)
    #for v in coord: print(v, coord[v])
    tmp = set()
    union_items = {}
    for y, v in coord.items():
        v.sort()
        prev = None
        for elem in v :
            if prev is None :
                prev = elem
            elif elem[0]<=prev[1] + 1:
                prev = (prev[0], max(elem[1], prev[1]) )
            else:
                for x in range(prev[1] + 1, elem[0]):
                    print(x * 4000000 + y) # output only one element 
                prev = (prev[0], elem[1])

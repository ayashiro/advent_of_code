import sys,re
with open(sys.argv[1]) as f:
    y_coord = int(sys.argv[2])
    lines = [line.strip() for line in f.readlines()]
    pat = re.compile(r"Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)")
    sensors = set()
    beacons = set()
    coord = {}
    for line in lines:
        m = pat.match(line)
        s_x, s_y = int(m.group(1)), int(m.group(2))
        b_x, b_y = int(m.group(3)), int(m.group(4))
        beacons.add((b_x, b_y))
        m_d = abs(s_x - b_x) + abs(s_y  - b_y)
        rest_md =  m_d - abs(s_y - y_coord)
        if rest_md < 0 :
            continue
        if y_coord not in coord:
            coord[y_coord] = []
        coord[y_coord].append((s_x - rest_md, s_x + rest_md + 1 ))
    tmp = set()
    for rng in coord[y_coord]:
        for s in range(*rng):
            if (s, y_coord) not in beacons:
                tmp.add(s)
    print(len(tmp))
        

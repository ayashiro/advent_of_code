import sys, re
with open(sys.argv[1]) as f :
    rate_map = {}
    adj_map = {}
    for line in f.readlines():
        pat = re.compile(r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)")
        m = pat.match(line.strip())
        valve = m.group(1)
        rate = int(m.group(2))
        adj = [v.strip() for v in  m.group(3).split(",")]
        rate_map[valve] = rate
        adj_map[valve] = adj
    valve_to_index = {}
    index_to_valve = []
    rate = []
    adj = [[] for _ in rate_map]
    for i,v in rate_map.items():
        if v != 0 :
            index_to_valve.append(i)
            valve_to_index[i] = len(valve_to_index)
            rate.append(rate_map[i])
    has_value = len(valve_to_index)
    for i, v in rate_map.items():
        if i not in valve_to_index:
            valve_to_index[i] = len(valve_to_index)
            index_to_valve.append(i)
            rate.append(rate_map[i])
    for k, v in adj_map.items():
        ind = valve_to_index[k]
        for t in v:
            adj[ind].append(valve_to_index[t])
    start = valve_to_index["AA"]    
    # prev[elephant][l][state]
    N = 26
    print(has_value , (1<<has_value) * N * len(rate_map) ** 2)
    prev = [[[-1 for _ in range(1<<has_value)] for _ in rate_map ] for _ in rate_map ]
    prev[start][start][0] = 0
    valve_to_flow = []    
    for i in range(1<<has_value):
        tmp = 0
        for t in range(has_value):
            if (i & (1<<t)) != 0: tmp += rate[t]
        valve_to_flow.append(tmp)
    print(rate,adj, valve_to_index , valve_to_flow)
    for t in range(N-1):
        print(t)
        current = [[[-1 for _ in range(1<<has_value)] for _ in rate_map ] for _ in rate_map ]
        for s in range(1<<has_value):        
            for l in range(len(rate_map)):
                for e in range(len(rate_map)):
                    if prev[l][e][s] < 0: continue
#                    print(f"current_s = {prev[l][e][s]:4d} time:{t:2d} state:{int(bin(s)[2:]):08d}, {index_to_valve[l]}, {index_to_valve[e]}, current_flow = {valve_to_flow[s]} ")                        
                    tmpe = []
                    tmpl = []
                    if rate[e] > 0 and ((1<<e)&s) == 0: tmpe = [e]
                    if rate[l] > 0 and ((1<<l)&s) == 0: tmpl = [l]
                    for e_adj in adj[e]  + tmpe:
                        for l_adj in adj[l] + tmpl:
                            new_state = s
                            additional_flow = 0
                            if e_adj == e :
                                new_state = new_state | (1<<e)
                                additional_flow += rate[e]
                            if l_adj == l :
                                new_state = new_state | (1<<l)
                                additional_flow += rate[l]
                            if e_adj == e and l_adj == l and l == e :
                                additional_flow = rate[e]
                            current[l_adj][e_adj][new_state] = max(current[l_adj][e_adj][new_state], prev[l][e][s] + additional_flow + valve_to_flow[s])
        prev = current
    ans = 0 
    for s in range(1<<has_value):
        for l in range(len(rate_map)):
            for e in range(len(rate_map)):
                ans = max(ans, current[l][e][s])
    print(ans)

            
    
        
        

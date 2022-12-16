import sys, re
with open(sys.argv[1]) as f :
    rate_map = {}
    adj_map = {}
    for line in f.readlines():
        pat = re.compile(r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)")
        m = pat.match(line.strip())
        print(m)
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
    # dp[state][location][time]
    N = 30
    dp = [[[-1 for _ in range(N+1)] for _ in rate_map ] for _ in range(1<<has_value)]
    dp[0][start][0] = 0
    valve_to_flow = []    
    for i in range(1<<has_value):
        tmp = 0
        for t in range(has_value):
            if (i & (1<<t)) != 0: tmp += rate[t]
        valve_to_flow.append(tmp)
    print(rate,adj, valve_to_index)
    for t in range(N):    
        for s in range(1<<has_value):        
            for l in range(len(rate_map)):
                if dp[s][l][t] < 0: continue
                if rate[l]  > 0 :
                    if ((1<<l) & s) == 0:
 #                       print(f"location = {index_to_valve[l]} state: {bin(s)[2:]} time : {t} state {valve_to_flow[s]} dp {dp[s][l][t]} release {index_to_valve[l]} to {rate[l]}")
                        dp[s|(1<<l)][l][t+1] = max(dp[s][l][t] + rate[l] + valve_to_flow[s], dp[s|(1<<l)][l][t+1]) # open valve
                for n in adj[l]:
#                    print(f"location = {index_to_valve[l]} state: {bin(s)[2:]}, time{t} v : {valve_to_flow[s]} dp {dp[s][l][t]} n {index_to_valve[n]}")
                    dp[s][n][t+1] = max(dp[s][n][t+1], dp[s][l][t] + valve_to_flow[s])
    ans = 0 
    for s in range(1<<has_value):
        for l in range(len(rate_map)):
            ans = max(ans, dp[s][l][N-1])
    print(ans)
            
    
        
        

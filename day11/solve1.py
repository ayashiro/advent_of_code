import sys


class Monkey():
    def __init__(self, ind,si, op, test_div, t, f):
        self.ind = ind
        self.si = si
        self.op = op
        self.test_div = test_div
        self.t = t
        self.f = f
with open(sys.argv[1]) as f :
    lines = [line.strip() for line in f.readlines()]
    monkeys = []
    modulos = 1
                                                                          
    for i in range(0, len(lines), 7):
        ind = int(lines[i].split()[1][:-1])
        si = list(int(x) for x in lines[i+1].split(":")[1].strip().split(","))
        x = f"lambda old :{lines[i+2].split('=')[-1]}"
        op = eval(x)
        test_div = int(lines[i+3].strip().split()[-1])
        t = int(lines[i+4].strip().split()[-1])
        f = int(lines[i+5].strip().split()[-1])
        modulos  *= test_div
        monkeys.append(Monkey(ind, si, op, test_div, t, f))
        print(ind, si, x ,op(10), test_div, t, f)
    print(modulos)
    times = [0] * len(monkeys)
    for i in range(10000):
        for monkey in monkeys:
            for v in monkey.si:
                times[monkey.ind] += 1
                v = monkey.op(v)
                ind = -1
                if v % monkey.test_div == 0:
                    ind = monkey.t
                else:
                    ind = monkey.f            
                monkeys[ind].si.append(v % modulos)
            monkey.si = []
        if (i+1) % 1000 == 0 or i == 19:
            print(times)

    print(times)
    times.sort()
    print(times[-1] * times[-2])

data = open("day16.input", "r")

class valve():
    def __init__(self, name, rate, tunnels):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels

    def __str__(self):
        return(f"Valve {self.name} flows at {self.rate} and goes to valves {self.tunnels}")

tunnel_map = {}
# Build up graph
for line in data:
    line = line.strip()
    contents = line.split()
    name = contents[1]
    rate = int(contents[4][5:-1])
    connected_valves = []
    for connected_valve in contents[9:]:
        connected_valves.append(connected_valve.strip(","))
    tunnel_map[name] = valve(name, rate, connected_valves)

seen_optimizations = {}

def optimize(time=30, opened=[], current_valve="AA"):
    optimization_tuple = (time, ','.join(sorted(opened)), current_valve)
    if optimization_tuple in seen_optimizations:
        return seen_optimizations[optimization_tuple]

    if time == 0:
        return 0

    new_release = 0
    for valve in opened:
        new_release += tunnel_map[valve].rate

    options = []
    if current_valve not in opened and tunnel_map[current_valve].rate != 0:
        options.append(optimize(time-1, 
                                opened + [current_valve], 
                                current_valve = current_valve))
    for new_valve in tunnel_map[current_valve].tunnels:
        options.append(optimize(time-1,
                                opened=opened,
                                current_valve = new_valve))

    best = max(options) + new_release
    seen_optimizations[optimization_tuple] = best
    return best

print(optimize())
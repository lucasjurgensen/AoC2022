data = open("test.input", "r")

class valve():
    def __init__(self, name, rate, tunnels):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels

    def __str__(self):
        return(f"Valve {self.name} flows at {self.rate} and goes to valves {self.tunnels}")

tunnel_map = {}
# Build up graph
# Huge optimization would be to remove useless valves
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

def optimize(time=5, opened=[], current_valves=["AA","AA"]):
    optimization_tuple = (time, ','.join(sorted(opened)), ','.join(sorted(current_valves)))
    if optimization_tuple in seen_optimizations:
        return seen_optimizations[optimization_tuple]

    if time == 0:
        return 0

    new_release = 0
    for valve in opened:
        new_release += tunnel_map[valve].rate

    options = []
    person = current_valves[0]
    elephant = current_valves[1]

    # Person opens
    if person not in opened and tunnel_map[person].rate != 0:
        # Elephant opens
        if elephant != person and elephant not in opened and tunnel_map[elephant].rate != 0:
            options.append(optimize(time-1,
                            opened[:] + [person, elephant],
                            current_valves = current_valves[:]))
        # Elephant moves
        for new_ephant in tunnel_map[elephant].tunnels:
            options.append(optimize(time-1,
                                    opened + [person],
                                    current_valves=[person, new_ephant]))

    # Person moves
    for new_person in tunnel_map[person].tunnels:
        # Elephant opens
        if elephant != person and elephant not in opened and tunnel_map[elephant].rate != 0:
            options.append(optimize(time-1,
                                    opened + [elephant],
                                    current_valves = [new_person, elephant]))
        # If elephant moves
        for new_ephant in tunnel_map[elephant].tunnels:
            options.append(optimize(time-1,
                                    opened,
                                    current_valves=[new_person, new_ephant]))

    best = max(options) + new_release
    seen_optimizations[optimization_tuple] = best
    return best

print(optimize())
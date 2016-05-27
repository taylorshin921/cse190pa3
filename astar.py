# astar implementation needs to go hereimport mathimport Queuedef astar(move_list, map_size, start, goal, walls, pits):    start = tuple(start)    goal = tuple(goal)    cameFrom = {}    cameFrom[start] = None    costRecent = {}    costRecent[start] = 0        # PQ keeps track of forward cost (uniform cost search)    frontier = Queue.PriorityQueue()    frontier.put(start, 0)    while not frontier.empty():        curr = frontier.get()        if curr == goal:            return path_sequence(cameFrom, curr)        for neighbor in neighbors(curr, move_list, map_size, walls, pits):            new_cost = costRecent[curr] + 1            if neighbor not in costRecent or new_cost < costRecent[neighbor]:                costRecent[neighbor] = new_cost                astar_val = new_cost + heuristic(neighbor, goal)                frontier.put(neighbor, astar_val)                cameFrom[neighbor] = curr    return 'Failure'""" Returns the optimal path sequence calculated by the A* algorithm """def path_sequence(cameFrom, curr):    sequence = [curr]    while curr in cameFrom.keys():        curr = cameFrom[curr]        sequence.insert(0, curr)    return sequence""" Returns the neighbors of a specific location that are valid """def neighbors(loc, move_list, map_size, walls, pits):    valid_neighbors = []    for move in move_list:        next = (loc[0] + move[0], loc[1] + move[1])        if is_inbounds(next, map_size) and not is_wallorpit(next, walls, pits):            valid_neighbors.append(next)    return valid_neighbors""" Check if given location is out of bounds """def is_inbounds(loc, map_size):    if (loc[0] >= 0 and loc[0] < map_size[0]) and (loc[1] >= 0 and loc[1] < map_size[1]):        return True    return False""" Check if location is a wall or pit """def is_wallorpit(loc, walls, pits):    for wall in walls:        if (loc[0] == wall[0]) and (loc[1] == wall[1]):            return True    for pit in pits:        if (loc[0] == pit[0]) and (loc[1] == pit[1]):            return True    return False""" Heuristic is the manhattan distance to the goal """def heuristic(loc1, loc2):    return math.fabs(loc1[0] - loc2[0]) + math.fabs(loc1[1] - loc2[1])
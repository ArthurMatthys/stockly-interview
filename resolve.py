import math


def read_file(filename):
    with open(filename, "r") as f:
        content = f.readlines()
    adj = [lines.replace("\n", "").split(",") for lines in content]
    max_weight = 0
    for i, line in enumerate(adj):
        for j, val in enumerate(line):
            if val == "-":
                adj[i][j] = math.inf
            else:
                adj[i][j] = int(val)
                max_weight += int(val)
    return adj, max_weight


def find_min(adj, lst_opened):
    min_paths = math.inf
    new_node = 0
    for opened in lst_opened:
        min_path = min(adj[opened])
        node_index = adj[opened].index(min_path)
        if min_path < min_paths:
            min_paths = min_path
            new_node = node_index
    return new_node, min_paths


def main(init):
    adj, max_weight = read_file("p107_network.txt")
    lst_opened = [init]
    tot_weight = 0
    while len(lst_opened) != len(adj):
        new_node, weight = find_min(adj, lst_opened)
        tot_weight += weight
        for opened in lst_opened:
            adj[opened][new_node] = math.inf
            adj[new_node][opened] = math.inf
        lst_opened.append(new_node)
    print(max_weight / 2 - tot_weight)


if __name__ == "__main__":
    for i in range(40):
        main(i)

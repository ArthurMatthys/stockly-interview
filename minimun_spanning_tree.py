import math


def read_file(filename):
    with open(filename, "r") as f:
        content = f.readlines()
    adj = [lines.replace("\n", "").split(",") for lines in content]
    paths = []
    max_weight = 0
    for i, line in enumerate(adj):
        for j, val in enumerate(line):
            if val != "-":
                paths.append((i, j, int(val)))
                max_weight += int(val)
    paths.sort(key=lambda x: x[2], reverse=True)
    return paths, max_weight, len(adj)


def main():
    paths, max_weight, size = read_file("p107_network.txt")
    new_weight = 0
    edges = []
    while True:
        start, end, weight = paths.pop()
        start_in = -1
        end_in = -1
        for i, edge in enumerate(edges):
            if start in edge:
                start_in = i
            if end in edge:
                end_in = i
        if start_in == -1 and end_in == -1:
            edges.append([start, end])
            new_weight += weight
        elif start_in > 0 and end_in == -1:
            edges[start_in.pop()].append(end)
            new_weight += weight
        elif (len(start_in) == 0 and len(end_in) > 0):
            edges[end_in.pop()].append(start)
            new_weight += weight
        else:
            intersect = set.intersection(start_in, end_in)
            if len(intersect) != 0:
                continue
            else:



        if len(edges) == 1 and len(edges[0]) == size:
            break
    print(max_weight - new_weight)


if __name__ == "__main__":
    main()

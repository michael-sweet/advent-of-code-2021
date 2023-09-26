with open('input.txt') as input_file:
    input_array = [x.split('-')
                   for x in input_file.read().split('\n')]


def buildGraph(a, b, graph):
    if a not in graph:
        graph[a] = []

    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)


def buildPaths(start_node, graph, current_path=[], paths=[], double_visit = False):
    if (start_node.islower() or start_node == 'start') and start_node in current_path:
        if start_node != 'start' and not double_visit:
            double_visit = True
        else:
            return paths

    current_path.append(start_node)

    if start_node == 'end':
        paths.append(current_path)
        return paths

    for connecting_node in graph[start_node]:
        paths = buildPaths(connecting_node, graph, current_path.copy(), paths, double_visit)

    return paths


graph = {}
for nodes in input_array:
    buildGraph(*nodes, graph)

paths = buildPaths('start', graph)

print(len(paths))

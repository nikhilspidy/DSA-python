#This program prints nodes in BFS manner

def bfs(graph, current):
    q = [current]

    while len(q) != 0:
        element = q.pop(0)
        print(element)
        for e in graph[element]:
            q.append(e)


if __name__ == '__main__':
    graph = {
        "a": ["b", "f", "e"],
        "b": ["c"],
        "c": ["d"],
        "d": ["e"],
        "e": [],
        "f": ["d"]
    };

    bfs(graph, "a");

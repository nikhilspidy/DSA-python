#This program prints nodes in DFS manner

def dfs(graph,current):
    print(current);

    for node in graph[current]:
        dfs(graph,node);



if __name__ == '__main__':
    graph = {
        "a":["b","f","e"],
        "b":["c"],
        "c":["d"],
        "d":["e"],
        "e":[],
        "f":["d"]
    };

    dfs(graph,"a");

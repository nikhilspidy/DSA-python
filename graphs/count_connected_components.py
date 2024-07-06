#This program checks if path exists from one to another

def count_connected_components(visited,graph,element):
    if element in visited:
        return visited;
    
    visited.add(element)

    for neighbour in graph[element]:
        if(neighbour not in visited):
            count_connected_components(visited,graph,neighbour)


    return visited;



if __name__ == '__main__':
    graph = {
        "3":[],
        "4":[6],
        "6":["4","5","7","8"],
        "8":["6"],
        "7":["6"],
        "5":["6"],
        "1":["2"],
        "2":["1"]
    };

    visited = set()
    for element in graph:
        visited = count_connected_components(visited,graph,element);

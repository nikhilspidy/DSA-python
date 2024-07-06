#This program checks if path exists from one to another

def check_if_path_exists(visited,graph,source,destination):
    if source == destination:
        return True;

    visited.add(source)

    for neighbour in graph[source]:
        if(neighbour not in visited):
            if check_if_path_exists(visited,graph,neighbour,destination) == True:
                return True


    return False;



if __name__ == '__main__':
    graph = {
        "i":["j","k"],
        "j":["i"],
        "k":["i","m","l"],
        "m":["k"],
        "l":["k"],
        "o":["n"],
        "n":["o"]
    };

    visited = set()
    print(check_if_path_exists(visited,graph,"i","n"))
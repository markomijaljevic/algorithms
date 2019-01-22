class Graph:
    def __init__(self):
        self.depthCounter = 1
        self.movies = []


class Node:
    def __init__(self,id,movieTitle,actorsList):
        self.id = id
        self.movieTitle = movieTitle
        self.actorsList = actorsList
        self.actorsListIterator = 0
        self.visited = False

def printNode(node):
    print()
    print(node.id)
    print("--------------------------------")
    print(node.movieTitle)
    print("--------------------------------")
    print(node.actorsList)
    print()

def printQueue(queue):
    with open("queue.txt","w") as q:
        for movie in queue:
            q.write(str(str(movie.id) + " -- " + movie.movieTitle + "\n"))


def findBaconNumber(graph,actor1,actor2):
    queue = [movie for movie in graph.movies if actor1 in movie.actorsList]
    last = queue[len(queue)-1] 

    while queue:
        #printQueue(queue)
        movie = queue[0]
        if actor2 in movie.actorsList and movie.visited == False:
            return graph.depthCounter 
        
        movie.visited = True

        if last == movie:
            graph.depthCounter += 1
            last = queue[len(queue)-1]

        for actor in movie.actorsList:
            if actor != actor1:
                for mov in graph.movies:
                    if actor in mov.actorsList and actor2 not in mov.actorsList and mov.visited == False:
                        mov.visited = True
                        queue.append(mov)
                    elif actor in mov.actorsList and actor2 in mov.actorsList:
                        return graph.depthCounter + 1

        del queue[0]

    return -1


def main():

    graph = Graph()
    actor1 = "Kevin Bacon"
    actor2 = "Keanu Reeves"
    id = 0

    with open("movies.txt","r") as movies:
        for line in movies:
            line = line.split(";")
            line[len(line)-1] = line[len(line)-1].strip("\n")
            graph.movies.append(Node(id,line[0],line[1:]))
            id += 1

    bacon = findBaconNumber(graph,actor1,actor2)
    print("Bacon number is: ",bacon)
    #print(bacon.movieTitle)

if __name__ == "__main__":
    main()

import sys

def getRoads(roads):
    roads = roads.split(" ")
    roads = [x.split(",") for x in roads]
    intRoads = []
    intRoad = []

    for road in roads: # pretvorba char u int
        for i in road:
            intRoad.append(int(i))
        intRoads.append(intRoad)
        intRoad = []

    return intRoads


def dijkstra(cities,start_city,target_city,roads):
    cities[start_city][1] = 0
    visited = [start_city]
    neighbors = []
    index = 0
    path = []

    while  True:
        if start_city != target_city: 
            for city in cities:
                if not city[0] in visited:
                    for road in roads:
                        if (road[0] == start_city or road[1] == start_city) and \
                            (road[0] == city[0] or road[1] == city[0]):

                            if road[2] + cities[start_city][1] < city[1]:
                                city[1] = road[2] + cities[start_city][1]
                                neighbors.append(city)
                                path.append(start_city)

                                
        try:
            neighbors.sort(key=lambda x: x[1]) 
            start_city = neighbors[index][0]
            visited.append(start_city)
            index += 1
        except IndexError:
            for city in neighbors:
                if city[0] == target_city:
                    print("Algorithm has finished searching!")
                    return city[1]

            return -1

        print("--------------------------------")
        print("Neighbors",neighbors)
        print("Visited",visited)
        print("Start City",start_city)
        print("Path",path)
        print("--------------------------------")

def main():

    N = 5
    surveying_cities = [2,3,2,4]
    roads = "0,2,4 0,1,2 2,1,2 1,3,3 4,0,4"
    roads = getRoads(roads)
    start_city = 0
    costs = 0

    while surveying_cities:
        cities = [[x,sys.maxsize] for x in range(0,N)]
        target_city = surveying_cities[0]

        print("Start city ->",start_city)
        print("Target city ->",target_city)

        cost = dijkstra(cities,start_city,target_city,roads)
        print("---------------------------------------------> Cost is",cost)

        if cost == -1 :
            print("It is impossible to survey them all!")
            return
        else:
            costs += cost
            cost = 0   

        start_city = target_city
        del surveying_cities[0]

    print("Cheapest path cost is", costs)

if __name__ == "__main__":
    main()
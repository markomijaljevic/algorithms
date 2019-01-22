import sys

def determineCost(N,cities,roads):
    roads = roads.split(" ")
    roads = [x.split(",") for x in roads] 
    costs = 0
    path = [x for x in range(0,N)]
    print("PATH:",path)
    starting_city = 0

    while cities:
        surveying_city = cities[0]
        connected_cities = []
        connection_with_next_city = 0
        cost = 0
        c = 0
        flag = False
        print("Surveying city ->",surveying_city)
        for city in path:
            if city != surveying_city:
                print("City ->",city)
                for road in roads:
                    #print(road)
                    if (int(road[0]) == surveying_city or int(road[1]) == surveying_city) and (int(road[0]) == city or int(road[1]) == city):
                        try:
                            next_surveying_city = cities[1]
                            for rd in roads:
                                #print("--->",rd)
                                if (int(rd[0]) == next_surveying_city or int(rd[1]) == next_surveying_city) and (int(rd[0]) == city or int(rd[1]) == city):
                                    connection_with_next_city += 1
                        except IndexError:
                                pass

                        if city > starting_city: 
                            print("Calculating new cost...")
                            for i in range(0,len(path)):
                                for rd in roads:
                                    if starting_city == surveying_city:
                                        flag = True
                                        break
                                    try:
                                        if (int(rd[0]) == path[starting_city] or int(rd[1]) == path[starting_city]) and (int(rd[0]) == path[starting_city+1] or int(rd[1]) == path[starting_city+1]):
                                            starting_city = path[starting_city+1]
                                            cost += int(rd[2])
                                    except IndexError:
                                        break
                                if flag:
                                    cost += int(road[2])
                                    connected_cities.append({city:(cost,connection_with_next_city)})
                                    break
                                else:
                                    pass
                        else:
                            connected_cities.append({city:(int(road[2]),connection_with_next_city)})    

                        connection_with_next_city = 0

        road_cost = sys.maxsize
        city_conn = 0 

        #-----------------------------------------------------------------------------#
        for conn_cities in connected_cities:
            print("-->",conn_cities)

            values = list(conn_cities.values())[0]

            if values[0] <= road_cost and values[1] >= city_conn : 
                chosen_city = list(conn_cities.keys())[0] 
                road_cost = values[0]
                city_conn = values[1]
            elif values[0] < road_cost and chosen_city < list(conn_cities.keys())[0]:
                chosen_city = list(conn_cities.keys())[0]
                road_cost = values[0]
                city_conn = values[1]
        #-----------------------------------------------------------------------------#
        print("Chosen citiy ->",chosen_city)
        print("Cost ->",road_cost)
        print("-----------------------")
        costs += road_cost
        del cities[0]     

    return costs
    


def main():
    '''
    https://community.topcoder.com/stat?c=problem_statement&pm=10782
    '''
    N = 5
    cities = [2,3,2,4]
    roads = "0,2,4 0,1,2 2,1,2 1,3,3 4,0,4"
    costs = determineCost(N,cities,roads)
    print("Costs are",costs)


if __name__ == "__main__":
    main()

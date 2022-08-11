# route-agent
Here I am explaining my code and logic startegy

Navigation (route_agent) :

        Question : Find shortest path between agent and you, considering the obstacles.
        Algorithm : A* Algorithm

        Strategy : 
        Modified the fringe to store directions traced along with the coordinates and distance travelled, so that my goal node in the fringe already have the path it traced till now. 
        Using a priority queue as my fringe data structure.
        List is maintained for keeping records of visited Nodes, to avoid infinite loop.
        Heuristic function : Manhattan Distance from goal Node, expanding the node having shortest distance.
        Whenever goal node is found, my search function returns (distance, direction), particular to that node.
        If my priority queue becomes empty, and no goal is achieved , my search function returns -1.

        Steps for code working:
        1. Find the pichu location : pichu_loc
        2. Find the goal location : destination_loc
        3. Create a empty List as visitedPairs to avoid infinite loop
        4. Create a fringe and put initial values to it : fringe = [((pichu_loc, 0 , ""), 0 )]. Fringe structure is defined as : [ ( ( pichuLocation, currentDistance, pathTraced ) , cost ) ]
            Where, 
            pichuLocation : current location of pichu or current pointer
            currentDistance : how much distance moved from initial position of pichu
            pathTraced : Directions from initial position of pichu
            cost : currentDistance + 1 + Manhattan Distance from goal node 

            We are using a priority queue as fringe data structure.
        5. while fringe : 
            1. Pop from queue as current node, and make an entry of it to visitedPairs list, to keep of track of nodes already visited
            2. check if current node == goal node ? return ( currentDistance, pathTraced )
            3. find all the possible moves, and for each possible move :
                    1. find its direction from previous state ( L, R, U, D ) as tempDirection
                    2. find cost, using cost = currentDistance + 1 + Manhattan Distance from goal node 
                    3. append node to the fringe  as ( possibleMove, currentDistance+1, pathTraced+ tempDirection), cost )
            4. sort the fringe according to cost( priority queue)
        6. return ( -1 , "" )

        Initial State : initial location of pichu
        Valid States : Set of all the nodes not having "X" or "@" placed
        Successor Function : Move Left, Right, Up, Bottom, when it is not an obstacle "X" / or itself the goal node "@"
        Cost Function : +1 for every move in any of the direction( except diagonal)
        Goal State : My location


#Run
python3 routeAgent.sh grid1.txt
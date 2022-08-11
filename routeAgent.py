import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        #store in fringe
        fringe= [((pichu_loc, 0 , ""), 0 )]

        #finding destination to write heusristic
        destination_loc = [(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="@"][0]

        visitedPairs= []

        #search algorithm
        while len(fringe) > 0:
                ( (curr_move, curr_dist, directions ), cost )= fringe.pop()

                visitedPairs.append( curr_move )

                if( curr_move[0] == destination_loc[0] and curr_move[1] == destination_loc[1]):
                        return( curr_dist, directions )

                possibleMoves = moves( house_map, *curr_move )

                if( len(possibleMoves)):
                        for move in possibleMoves:
                                if move not in visitedPairs: 
                                        cost = curr_dist + 1 + abs( move[0] - destination_loc[0]) + abs( move[1] - destination_loc[1])

                                        if( move[0] == curr_move[0] -1 ):
                                                tempDirection = "U"
                                        elif( move[0] == curr_move[0] + 1):
                                                tempDirection = "D"
                                        elif( move[1] == curr_move[1] -1 ):
                                                tempDirection = "L"
                                        else:
                                                tempDirection = "R"
                                        
                                        fringe.append( ( ( move, curr_dist+1, directions+ tempDirection), cost ))
                        fringe.sort(reverse=True) #Reference for this line of code is taken from Python documentation : https://pythonguides.com/priority-queue-in-python/
        return ( -1, "" )
                        



# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])


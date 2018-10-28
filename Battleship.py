import math

def calc(shipsExpand,T):
    """
    Function calculates number of sunken and damaged ships
    """
    hits = T.split(" ") # convert string to list
    shipHit = 0
    h = 0 # damaged ships counter
    sunk = 0 # sunken ships counter
  
    for ship in shipsExpand: 
        shiplist = ship.split(" ") # convert string to list
        for hit in hits:
            if hit in shiplist: # if ship is damaged
                del shiplist[shiplist.index(hit)] # delete cell ( position ) from list
                shipHit = 1 # count hit
        
        if not shiplist: # if ship is destroyed, counter += 1
            sunk += 1
            shipHit = 0
        elif shipHit > 0: #if ship is damaged
            h += 1
            shipHit = 0

    return str(sunk)+","+str(h) # return string of sunk and damaged ships

def solution(N,S,T):
    """
    Function that reveals all played cells
    """

    S = str.upper(S) # make sure that letters are uppercase
    T = str.upper(T) # make sure that letters are uppercase
    
    ships = S.split(',') # convert string to list
    shipsExpand = [] # list of all ships positions
    
    for ship in ships:
 
        row = ship.split() # list of rows
        col = ship.split() # list of cols
        col = [s[-1] for s in row] # get column id ( letters )
        row = [s[:-1] for s in row] # get row id ( numbers )
        #print("row->", row , "Col -> ",col)

        # if ship is in just one cell
        if col[0] == col[1] and row[0] == row[1]:
            ship = ship.replace(" " + row[0] + col[0],"") # values are same, add just one to new list
            shipsExpand.append(ship)
            continue

        #if ship is in same column and is placed on more then two cells
        elif col[0] == col[1] and ((int(row[1]) - int(row[0])) > 1 ):

            numsBetween = (int(row[0]) + int(row[1])) / 2 # magic formula to reveal missing numbers   
            
            if not float(numsBetween).is_integer(): # if number is not natural number ( number is decimal )
                num1 = int(numsBetween) #round to lesser value
                num2 = math.ceil(numsBetween) #round to higher value
                ship = ship + " " + str(num1) + col[0] + " " + str(num2) + col[0] # expand current string ( add revealed position )
                shipsExpand.append(ship)
                continue
            else:    # if number is natural number 
                ship = ship + " " + str(int(numsBetween)) + col[0]  # expand current string ( add revealed position )
                shipsExpand.append(ship)
                continue
    	# if row numbers are same, ship is placed in the same row and if distance is higher then one ( find missing column letters )
        elif row[0] == row[1] and (ord(col[1]) - ord(col[0])) > 1:
            # ord function to extract number representation of letter ( ASCII )
            lettersBetween = (ord(col[1]) + ord(col[0])) / 2 # magic formula to reveal missing letters  
            
            if not float(lettersBetween).is_integer(): # if number is not natural number ( number is decimal )
                lett1 = chr(int(lettersBetween)) #round to lesser value
                lett2 = chr((math.ceil(lettersBetween))) #round to higher value ( char funciton to get letter from number (ASCII) )
                ship = ship + " " + row[0] + lett1  + " " + row[0] + lett2  # expand current string ( add revealed position )
                shipsExpand.append(ship)
                continue
            else:   # if number is natural number 
                ship = ship + " " + row[0] + chr(int(lettersBetween)) # expand current string ( add revealed position )
                shipsExpand.append(ship)
                continue

        elif row[0] != row[1] and col[0] != col[1]: #if letters and numbers in string are different ( 1B 2C )
            pos1 = row[0] + col[1] # reveal position 
            pos2 = row[1] + col[0] # reveal position 
            ship = ship + " " + pos1 + " " + pos2 # expand current string ( add revealed position )
            shipsExpand.append(ship)
            continue 

        shipsExpand.append(ship) # add all other ships 

    return calc(shipsExpand,T) 

def main():
    #N = 4 # number of columns
    S = "1B 3B,122D 124D,12C 12C,1A 2B" # string format of played positions
    T = "2B 2D 3D 4D 4A 1A 2A 1B 12C"  # string format of played targeted positions

    print(solution(N,S,T)) # print result


if __name__ == '__main__':
    main()
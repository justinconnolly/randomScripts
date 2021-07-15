from random import randint

#randomize the doors
def setTheStage():
    doors = [False,False,False]
    doors[randint(0,2)] = True
    return doors

#reveal a non-winning door -- this needs to be redone
def revealDoor(doors: list, userSelection: int, winningSelection: int):
    numberedDoors = [0,1,2]
    if userSelection != winningSelection:
        numberedDoors.remove(userSelection)
        numberedDoors.remove(winningSelection)
        return numberedDoors[0]
    else:
        numberedDoors.remove(userSelection)
        return numberedDoors[randint(0,1)]

def doSwitch(doors: list, selection:int, openedDoor: int):
    numberedDoors = [0,1,2]
    numberedDoors.remove(selection)
    numberedDoors.remove(openedDoor)
    return numberedDoors[0]
    
def MontyHall(switch: bool):
    stage = setTheStage()
    #print(stage)
    userSelection = randint(0,2)
    #print("User selection: " + str(userSelection))

    winningSelection = stage.index(True)
    #print("Winning door: " + str(winningSelection))
    openedDoor = revealDoor(stage,userSelection,winningSelection)
    #print("Revealed door: " + str(openedDoor))
    switchedDoor = doSwitch(stage, userSelection, openedDoor)
    #print("Switched to door: " + str(switchedDoor))
    if switch and stage[switchedDoor] or stage[userSelection]:
        #print("Winner!")
        return 1
    else:
        #print("Loser!")
        return 0
        
winners = 0
numberOfGames = 100000
switch = False
for x in range(numberOfGames):
    winners += MontyHall(switch)
winRate = winners/numberOfGames
print("The overall winrate after {} games,{} taking the switch when offered, is {}".format(numberOfGames,"" if switch else " not",winRate))

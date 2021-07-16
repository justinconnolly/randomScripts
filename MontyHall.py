from random import randint

#randomize the doors
def setTheStage() -> list:
    doors = [False,False,False]
    doors[randint(0,2)] = True
    return doors

#reveal a non-winning door -- this needs to be redone
def revealDoor(doors: list, userSelection: int, winningSelection: int) -> int:
    numberedDoors = [0,1,2]
    if userSelection != winningSelection:
        return 3 - userSelection - winningSelection
    else:
        numberedDoors.remove(userSelection)
        return numberedDoors[randint(0,1)]
    
def MontyHall(switch: bool) -> int:
    stage = setTheStage()
    userSelection = randint(0,2)
    winningSelection = stage.index(True)
    openedDoor = revealDoor(stage,userSelection,winningSelection)
    switchedDoor = 3 - userSelection - openedDoor
    if switch and stage[switchedDoor]:
        return 1
    elif not switch and stage[userSelection]:
        return 1
    else:
        return 0
        
winners = 0
numberOfGames = 100000
switch = True
for x in range(numberOfGames):
    winners += MontyHall(switch)
winRate = winners/numberOfGames

print("The overall winrate after {} games, {}taking the switch when offered, is {}.".format(numberOfGames, "" if switch else "not ",winRate))

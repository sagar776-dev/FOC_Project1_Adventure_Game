import json
import sys

# Player class to handle player data and cmds


class Player:
    def __init__(self, name, adventureMap):
        self.name = name
        self.inventory = list()
        self.adventureMap = adventureMap
        self.cmds = {
            "look": "Take a look at the current room",
            "go": "Go to a particular direction",
            "inventory": "View items in your inventory",
            "get": "Pick up an item/items",
            "drop": "Drop an item from your inventory",
            "quit": "Quit the game",
            "help": "Get help on cmds",
        }
        self.cmds_no_args = ["look", "quit", "help", "inventory"]
        self.cmds_args = ["go", "get", "drop"]
        self.currentRoomNo = 0
        self.currentRoom = adventureMap[0]

    def printHelp(self):
        print('You can run the following commands:')
        for cmd in self.cmds_no_args:
            print("  "+cmd)
        for cmd in self.cmds_args:
            print("  "+cmd + " ...")

    def roomLookUp(self):
        win_lose = ""
        flag = True
        endFlag = False
        if ('required' in self.adventureMap[self.currentRoomNo]):
            for item in self.adventureMap[self.currentRoomNo]['required']:
                if item not in self.inventory:
                    flag = False
                    break
            if flag:
                win_lose = self.adventureMap[self.currentRoomNo]['win']
            else:
                win_lose = self.adventureMap[self.currentRoomNo]['lose']
                endFlag = True

        print("> "+self.adventureMap[self.currentRoomNo]['name']+"\n")
        print(self.adventureMap[self.currentRoomNo]['desc']+"\n")
        if 'items' in self.adventureMap[self.currentRoomNo]:
            if(len(self.adventureMap[self.currentRoomNo]['items']) != 0):   
                print("Items:", end="")
                # print(*self.adventureMap[self.currentRoomNo]['items'], sep=", ")
                itemStr = ""
                for item in self.adventureMap[self.currentRoomNo]['items']:
                    itemStr += " "+item + ","
                if itemStr.endswith(","):
                    itemStr = itemStr[:-1]
                print(itemStr)
                print()
        if 'exits' in self.adventureMap[self.currentRoomNo]:
            if(len(self.adventureMap[self.currentRoomNo]['exits']) != 0):
                exitStr = "Exits:"
                # print("Exits:", *
                #       self.adventureMap[self.currentRoomNo]['exits'], sep=" ")
                for exit in self.adventureMap[self.currentRoomNo]['exits']:
                    exitStr+=" "+exit
                print(exitStr)
                print()
        if (len(win_lose) > 0):
            if (len(self.adventureMap[self.currentRoomNo]['exits']) == 0):
                endFlag = True
            print(win_lose)
            print()
        
        return endFlag

    def printPlayerInventory(self):
        if(len(self.inventory) == 0):
            print("You're not carrying anything.")
            return
        print("Inventory:")
        # print(*self.inventory, sep="\n  ")
        for item in self.inventory:
            print("  "+item)

    def addItemToInventory(self, item):
        if 'items' not in self.currentRoom:
            print(f"There's no {item} anywhere.")
            return
        if item not in self.currentRoom['items']:
            print(f"There's no {item} anywhere.")
            return
        self.inventory.append(item)
        itemIndex = self.adventureMap[self.currentRoomNo]['items'].index(item)
        self.adventureMap[self.currentRoomNo]['items'].pop(itemIndex)
        self.currentRoom = self.adventureMap[self.currentRoomNo]
        print("You pick up the " + item + ".")

    # def dropItemFromInventory(self, item):
    #     if item not in self.inventory:
    #         print('Item not in your inventory')
    #         return
    #     if 'items' not in self.currentRoom:
    #         self.adventureMap[self.currentRoomNo].items = list()
    #     itemIndex = self.inventory.index(item)
    #     self.inventory.pop(itemIndex)
    #     self.adventureMap[self.currentRoomNo]['items'].append(item)
    #     print("Dropped ", item)

    def goToDirection(self, direction):
        if 'exits' not in self.currentRoom:
            print(f"There's no way to go {direction}.")
            return
        if direction not in self.currentRoom['exits']:
            print(f"There's no way to go {direction}.")
            return
        print('You go '+direction+".\n")
        self.currentRoomNo = self.currentRoom['exits'][direction]
        self.currentRoom = self.adventureMap[self.currentRoomNo]
        return self.roomLookUp()


def processDirection(direction):
    direction = direction.lower()
    directions = ['north', 'south', 'east', 'west',
                  'northeast', 'southeast', 'northwest', 'southwest']
    dirAbbreviationMap = {
        'ne': 'northeast',
        'nw': 'northwest',
        'se': 'southeast',
        'sw': 'southwest',
    }
    if direction in directions:
        return [direction]
    if direction in dirAbbreviationMap:
        return [dirAbbreviationMap[direction]]
    dirList = list()
    for dir in directions:
        if dir.startswith(direction):
            dirList.append(dir)
    return dirList


def processCmd(cmd, player):
    # print(cmd)
    processedList = list()
    cmdList = cmd.lower()
    # print(list(player.cmds.keys()))
    commands = list(player.cmds.keys())
    for c in commands:
        if c.startswith(cmd):
            processedList.append(c)
    # print(processedList)
    return processedList

# Method to load the map file and start the game


def startGame(mapfile):
    # Load the JSON file
    with open(mapfile) as f:
        loop = json.load(f)

    # name = input("Input your name: ")
    player = Player("Sagar", loop)

    cmd = ""

    player.roomLookUp()

    while cmd.lower() != 'quit':
        try:
            cmdInput = input('What would you like to do? ')

            cmdList = cmdInput.lower().split(" ")
            if (len(cmdList) == 1):
                direction = processDirection(cmdList[0].strip().lower())
                if(len(direction) == 1):
                    flag = player.goToDirection(direction[0])
                    if flag:
                        break
                    continue
            cmd = cmdList[0].strip().lower()
            args = cmdList[1:]
            argStr = ' '.join(args)

            cmds = processCmd(cmd, player)
            if len(cmds) == 1:
                cmd = cmds[0]
            elif len(cmds) == 0:
                print('Invalid cmd')
                continue
            else:
                print('Did you mean: ', end='')
                print(*cmds, sep=", ")
                continue

            #print("Cmd entered: ", cmd)
            if cmd.lower().startswith('go'):
                # print(args)
                args = ' '.join(args).strip()
                if (len(args) == 0):
                    print("Sorry, you need to 'go' somewhere.")
                    continue
                # direction = processDirection(args)
                direction = args.lower()
                flag = player.goToDirection(direction)
                if flag:
                    break

            elif cmd.lower().startswith('get'):
                if (len(args) == 0):
                    print("Sorry, you need to 'get' something.")
                    continue
                for item in argStr.split(","):
                    player.addItemToInventory(item.strip())

            # elif cmd.lower().startswith('drop'):
            #     if (len(args) == 0):
            #         print("Itemname required for 'drop' cmd")
            #         continue
            #     for item in args:
            #         player.dropItemFromInventory(item)

            elif cmd.lower().startswith('inventory'):
                player.printPlayerInventory()

            elif cmd.lower().startswith('look'):
                player.roomLookUp()

            elif cmd.lower().startswith('help'):
                player.printHelp()

            elif cmd.lower().startswith('quit'):
                print('Goodbye!')
                break

            else:
                print('Please enter a valid cmd. Here is a list of commands.\n')
                player.printHelp()
        except EOFError:
            print("Use 'quit' to exit.")
        except Exception as e:
            print('Error: ', e)
            break

startGame(sys.argv[1])

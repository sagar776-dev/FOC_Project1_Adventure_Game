Sagar Chakravarthy Mathada Veera - 20011401

The URL of your public GitHub repo: 

    URL: https://github.com/sagar776-dev/FOC_Project1_Adventure_Game

An estimate of how many hours you spent on the project:

    3-4 hours for coding, 4 for debugging and formatting the code to pass autograder testcases

A description of how you tested your code:

    Manual testing for each cmd, and then overall testing with all cmds.

Any bugs or issues you could not resolve:

    Win/lose extension was a little tricky to design. but once I decided on the design and how I will implement the design, it was easy to code.

    There were no issues I could not resolve

An example of a difficult issue or bug and how you resolved:

     Once I designed the win/lose extension, it was easy to code.

A list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them 
(i.e., what are the new verbs/features, how do you exercise them, where are they in the map) :

    1. 'help' cmd:
        'help' cmd can be executed to get a list of all the executable cmds. The output is generated dynamically using the list of cmds.
        CMD syntax: 'help'

        -> You can use this cmd anywhere on the map.

    2. 'drop' cmd:
        You can execute 'drop itemname' cmd to drop an item from your inventory into the present room.

        CMD syntax: 'drop itemname'
        Ex:         'drop apple' --> will drop the 'apple' item from your inventory

        'drop' cmd can be used in any room to drop an item to the current room. If you don't the item in the inventory, the cmd will throw an error saying you don't have that item in your inventory.
    
    3. 'win/lose'
        The code can also handle adventure game with maps that have a win/lose conditions for the player. My custom game has two rooms that involve the conditions that decide if the player wins/loses that battle. There are three fields needed in the particular room for this to work. The fields are,

        I. Requirements: This is a list of items that the player need to posses in their inventory to win the battle in the room. The player needs to have all the items from the 'requirements' list to win the round.
        II. 'win' description: This is a description that is displayed if the player wins the battle in that room.
        III. 'lose' description: This is a description that is displayed if the player loses the battle in that room.

        -> There are two boss battles on my map

            I. Witch Queen: Boss battle in room 6
            ---> This is the first boss battle of this map. Witch queen can be found in room 6 of the map.
                To defeat her, you must posses the magic wand.
                You can obtain the 'wand' in room 4.
                As you can see from the map file, you'll see that the 'requirements' list requires you to have the 'wand' in your inventory to win this battle.

                If you win this round, the 'win' message will be displayed, and the game continues. At this stage, you'll be only allowed to travel to the room 7 to face the enchanted knight. So make sure you have the magic-blade-oil.
                If you lose this round, the 'lose' message is displayed and the game ends.

            II. Enchanted Kinght: Final Boss battle in room 7
            ---> This is the final boss battle of this map. Enchanted kinght can be found in room 7 of the map.
                To defeat the knight, you need to be in posession of magic blade oil and the enchanted sword.
                You can obtain 'magic-blade-oil' in room 3, in the mage's hut. Once you enter room three, the mage will prepare the blade oil for you. All you need to do is get if from her (get the item from the room using 'get magic-blade-oil')
                You can get the enchanted sword in room 5

                If you win this round, the 'win' message (epilogue) will be displayed, and the game ends.
                If you lose this round, the 'lose' message is displayed and the game ends.


            Steps to win the game are as follows: (for your easy evaluation)

                1. go south (or south), whichever you fancy
                2. go south
                3. get magic-blade-oil
                4. go west
                5. get wand
                6. go east
                7. get enchanted-sword
                8. go southwest
                9. go south
            
            You can get the losing condition if you don't pick up the required items mentioned above.

        (Optional extension - I wrote the code for this before drop cmd, and decided to keep it instead of removing the code. You can test the extension, or ignore it.
            4. Directions as verbs:
            You can use direction as a verb to go a particular way. 
            For example,

                >'north' is same as >'go north'

            Only 8 traditional directions can work as direction verbs, them being:
                --> north, east, south, west, northeast, southeast, southwest and northwest.
                For custom directions( if you choose to use directions like 'left', and like in some SciFI games, 'up' or 'down', you'll need the go keyword), you'll need to use 'go' cmd.

            The directions only work for full matches, not for abbreviations.

            CMD syntax: '[direction]'
            Ex:         'north' --> 'go north'
        )


Github URL mentioned below, and the code submitted to Gradescope

    URL: https://github.com/sagar776-dev/FOC_Project1_Adventure_Game


Cmd to execute and start the game:

    > python3 adventure.py adventure_game.map 


Map file name: adventure_game.map
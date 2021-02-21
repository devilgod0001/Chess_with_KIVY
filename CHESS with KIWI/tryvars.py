# Width and Height of window
b, h = 9*40, 16*40

x = [9, 53.25, 97.5, 141.75, 186, 230.25, 274.5, 318.75]

y = [149, 193.25, 237.5, 281.75, 326, 370.25, 414.5, 458.75]


'''# posns list must be improved for dynamic function of app with diferent screen resolutions '''

posns = [
    [ [9, 149 ], [53.25, 149 ], [97.5, 149 ], [141.75, 149 ], [186, 149 ], [230.25, 149 ], [274.5, 149 ], [318.75, 149 ]],
    [ [9, 193.25 ], [53.25, 193.25 ], [97.5, 193.25 ], [141.75, 193.25 ], [186, 193.25 ], [230.25, 193.25 ], [274.5, 193.25 ], [318.75, 193.25 ]],
    [ [9, 237.5 ], [53.25, 237.5 ], [97.5, 237.5 ], [141.75, 237.5 ], [186, 237.5 ], [230.25, 237.5 ], [274.5, 237.5 ], [318.75, 237.5 ]],
    [ [9, 281.75 ], [53.25, 281.75 ], [97.5, 281.75 ], [141.75, 281.75 ], [186, 281.75 ], [230.25, 281.75 ], [274.5, 281.75 ], [318.75, 281.75 ]],
    [ [9, 326 ], [53.25, 326 ], [97.5, 326 ], [141.75, 326 ], [186, 326 ], [230.25, 326 ], [274.5, 326 ], [318.75, 326 ]],
    [ [9, 370.25 ], [53.25, 370.25 ], [97.5, 370.25 ], [141.75, 370.25 ], [186, 370.25 ], [230.25, 370.25 ], [274.5, 370.25 ], [318.75, 370.25 ]],
    [ [9, 414.5 ], [53.25, 414.5 ], [97.5, 414.5 ], [141.75, 414.5 ], [186, 414.5 ], [230.25, 414.5 ], [274.5, 414.5 ], [318.75, 414.5 ]],
    [ [9, 458.75 ], [53.25, 458.75 ], [97.5, 458.75 ], [141.75, 458.75 ], [186, 458.75 ], [230.25, 458.75 ], [274.5, 458.75 ], [318.75, 458.75 ]]
    ]


'''  Initial Positions  '''

Default_Pos = {"HorseL":posns[0][1], "HorseR":posns[0][6], "King":posns[0][4], "CamelL":posns[0][2],
               "CamelR":posns[0][5], "ElephantL":posns[0][0], "ElephantR":posns[0][7], "Queen":posns[0][3],
               "Soldier1":posns[1][0], "Soldier2":posns[1][1], "Soldier3":posns[1][2], "Soldier4":posns[1][3],
               "Soldier5":posns[1][4], "Soldier6":posns[1][5], "Soldier7":posns[1][6], "Soldier8":posns[1][7]}


'''  Position Manager  '''
#           ElephantL    HorseL       CamelL       Queen        King         CamelR       HorseR       ElephantR
Pos_man = [posns[0][0], posns[0][1], posns[0][2], posns[0][3], posns[0][4], posns[0][5], posns[0][6], posns[0][7],
            posns[1][0], posns[1][1], posns[1][2], posns[1][3], posns[1][4], posns[1][5], posns[1][6], posns[1][7]]
#           Soldier1     Soldier2     Soldier3     Soldier4     Soldier5     Soldier6     Soldier7     Soldier8

'''  Colors  [All hex values]'''

Circle_color = "#D72638"
Window_back_color = "#47DDFF"
Boxes_color = "#FFFFFF"
Board_color = "#0B0500"

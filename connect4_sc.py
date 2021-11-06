def winlistmaker(): #makes a list of all possible win combinations
    
    for i in range(0,n**2):
        winlists.append([])
    s = [] #all possible values of rows/columns
    for i in range(1,n+1):
        s.append(i)
       
        
    def listmaker(stx,sty): #makes a list of 4 winning indices 
        li = []
        startval = (stx-1)+(sty-1)*n
        index = (x-1)+(y-1)*n
        
        if decider == 1: # horizontal
            for i in range(0,4):
                li.append(startval+i)
                
        elif decider == 2: # vertical
            for i in range(0,4*n,n):
                li.append(startval+i)
                
        elif decider == 3: # rightwards diagonal
            for i in range(0,4*n+4,n+1):
                li.append(startval+i)

        elif decider == 4: # leftwards diagonal
            for i in range(0,4*n-4,n-1):
                li.append(startval+i)
        winlists[index].append(li)
        

    for x in range(1,n+1): 
        for y in range(1,n+1):
            #horizontal
            for j in range(3,-1,-1):
                if ((x+j) in s) and ((x+(j-3)) in s):
                    decider = 1
                    listmaker((x+(j-3)),y)
                    
                    
            #vertical
            for j in range(3,-1,-1):
                if ((y+j) in s) and ((y+(j-3)) in s):
                    decider = 2
                    listmaker(x,(y+(j-3)))
                    
                    
            #rightwards diagonal
            for j in range(3,-1,-1):
                if (((x+j) in s) and ((y+j) in s)) and (((x+(j-3)) in s) and ((y+(j-3)) in s)):
                    decider = 3
                    listmaker((x+(j-3)),(y+(j-3)))

            #leftwards diagonal
            for j in range(3,-1,-1):
                if (((x+j) in s) and ((y-j) in s)) and (((x+(j-3)) in s) and ((y+(3-j)) in s)):
                    decider = 4
                    listmaker((x+j),(y-j))

def printboard(): #prints the current status of the game board
    
    q = 0
    for i in range(1,2*n+4):
        
        if i == 1 or i == 2*n+3: #column numbering
            for j in range(1,n+1):
                if j < 10:
                    print("  ",j," ",end="")
                if j >= 10:
                    print(" ",j," ",end="")
            print()
            
        elif i == 2 or i == 2*n+2: #equals
            print(equals)
            
        elif i%2 == 0: #separators of boxes
            print(plus)
            
        else:
            for j in range(0,n): #boxes
                print("| ",el[q+j]," ",end="")
            print("|")
            q = q + n
            
def gamemaster(p,a): #Inputs and executes moves

    var1 = True
    while var1 == True:
        
        var1 = False 
        print (p,", in which column would you like to play your move?")
        column = int(input())
        
        if  column < 1 or column > n: #error handling
            print("Please enter a valid column to play in!")
            var1 = True
            
        elif currentrow[column-1] in lastrow:
            print("There is no more space in this column...please play choose another one to play your move!")
            var1 = True
            
        else: #inputting of the game characters in the elements
             el[currentrow[column-1]] = a
             currentrow[column-1] = currentrow[column-1] - n
             
    return column

def winchecker(p,a,column): #checks for a winning move or a draw
    
    index = currentrow[column-1] + n
    count = 0
    finish = 0
    
    for li in winlists[index]:
        
        for i in li:
            if el[i] == a:
                count = count + 1
                
        if count == 4:
            print(p,"HAS WON THE GAME!!!")
            finish = 1
            break
            
        else:
            count = 0
            if currentrow == lastrow:
                print("DRAW!!!")
                finish = 1
                break
            
    return finish
    
#PRE-GAME SCREEN

import time

print("LAUNCHING GAME>>> ",end='')
for i in range(3,0,-1):
    time.sleep(1)
    print(i,"...",sep='',end='\r')
time.sleep(1)
print("GO!")

title = ["***********************************************************************************************************************************",\
         "***********************************************************************************************************************************",\
         "*******         _______  ____________  ____       __  ____       __  ___________      _______  ____________        ____     *******",\
         "*******        ********  ************  ****       **  ****       **  ***********     ********  ************        ****     *******",\
         "*******       **         **        **  ****       **  ****       **  **             **              **            ** **     *******",\
         "*******      **          **        **  ** **      **  ** **      **  **            **               **           **  **     *******",\
         "*******     **           **        **  **  **     **  **  **     **  **           **                **          **   **     *******",\
         "*******     **           **        **  **   **    **  **   **    **  ***********  **                **         **    **     *******",\
         "*******     **           **        **  **    **   **  **    **   **  ***********  **                **        **_____**     *******",\
         "*******     **           **        **  **     **  **  **     **  **  **           **                **       **********     *******",\
         "*******      **          **        **  **      ** **  **      ** **  **            **               **               **     *******",\
         "*******       **_______  **________**  **       ****  **       ****  **_________    **_______       **               **     *******",\
         "*******        ********  ************  **        ***  **        ***  ***********     ********       **               **     *******",\
         "*******                                                                                                                     *******",\
         "***********************************************************************************************************************************",\
         "***********************************************************************************************************************************",]
titlevar = [-5,-4,-3,-2,-1,16,17,18,19,20]
for i in range(-5,21):
    if i in titlevar:
        print()
    else:
        print(title[i])
    time.sleep(0.25)
         

#GAME PARAMETERS INPUT

qans = str(input("Do you know how to play connect four? yes/no"))
if qans == "no":
    print("First choose your grid size, number of players and game characters. Then the objective of the game is simple: the first player to form a vertical, horizontal or diagonal stack of 4 coins of ones own character wins the game.")

print('''



Recommended combinations:


GRID SIZE | NO. of
          | PLAYERS
====================
| 6 - 7   |   2    |
|---------+--------|
| 8 - 9   |   3    |
|---------+--------|
|   > 9   | > 3    |
====================
''')

n = int(input("In what grid size would you like to play? (nxn)"))
pnum = int(input("How many people are playing?"))
pname = []
pavatar = []
choose = True
for i in range(1,pnum+1):
    print("Player",i,",enter your name: ", end ='')
    x1 = str(input())
    while choose == True: #error handling
        choose = False
        x2 = str(input("Enter your character: "))
        if x2 in pavatar:
            print("This character has already been chosen! Please choose a different one!")
            choose = True
            
    pname.append(x1)
    pavatar.append(x2)
    choose = True

#GAME SETUP
    
winlists = [] 
winlistmaker()
column = 0

el = [] #list where the game events are stored
for i in range(0,n**2):
    el.append(' ')

currentrow = [] #list where index of bottomost unoccupied box is stored
for i in range((n**2)-n,n**2):
    currentrow.append(i)
    
lastrow = [] #error handling in case of full filled columns
for i in range(-n,0):
    lastrow.append(i)
    
plus = '|' #prestoring certain print elements to increase speed 
for i in range(1,n):
    plus = plus+ "-----+"
plus = plus + "-----|"
equals = ''
for i in range(0,6*n+1):
    equals = equals + "="
    

#GAME START
    
win = False
var99 = 0
printboard()
while win == False:
    win = True
    for i in range(0,pnum):
        column = gamemaster(pname[i],pavatar[i])
        printboard()
        finisher = winchecker(pname[i],pavatar[i],column)
        if finisher != 1:
            win = False
        else:
            var99 = 1
            break
    if var99 == 1:
        break
    
    

























































 

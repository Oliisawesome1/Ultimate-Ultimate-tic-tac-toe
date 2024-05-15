import random
from tkinter import *

intD = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8, ]

allowed = []
turn = "X"
coolnumber=1
def on_enter(e):
    for window in allbuttons:
        for game in allbuttons[window]:
            for square in allbuttons[window][game]:
                if e.widget == allbuttons[window][game][square]:
                    pathway=[window,game,square]
                    if allcolours[window][game][square]=="green" and e.widget.cget("text")=="  ":
                        print(checkall(allbuttons[pathway[1]][pathway[2]]))
                        if checkall(allbuttons[pathway[1]])!="  ":
                            for window in allbuttons:
                                for game in allbuttons[window]:
                                    if checkall(allbuttons[window][game])=="  ":
                                        for square in allbuttons[window][game]:
                                            allbuttons[window][game][square].config(highlightbackground="purple",bg="purple")

                        elif checkall(allbuttons[pathway[1]][pathway[2]])=="  ":
                            for square in allbuttons[pathway[1]][pathway[2]]:
                                allbuttons[pathway[1]][pathway[2]][square].config(highlightbackground="purple",bg="purple")
                        else:
                            for game in allbuttons[pathway[1]]:
                                if checkall(allbuttons[pathway[1]][game])=="  ":
                                    for square in allbuttons[pathway[1]][game]:
                                        allbuttons[pathway[1]][game][square].config(highlightbackground="purple",bg="purple")

def on_leave(e):
    #print(e.widget)
    for window in allbuttons:
        for game in allbuttons[window]:
            for square in allbuttons[window][game]:
                if e.widget == allbuttons[window][game][square]:
                    pathway = [window, game, square]
                    for window in allbuttons:
                        for game in allbuttons[window]:
                            for square in allbuttons[window][game]:
                                allbuttons[window][game][square].config(highlightbackground=allcolours[window][game][square],bg=allcolours[window][game][square])
    #allbuttons[mypath[0]][mypath[1]][mypath[2]].config(highlightbackground="orange")

def checkall(mydic):
    current = ""

    for thing in mydic:
        if isinstance(mydic[thing], dict):
            check = checkall(mydic[thing])
        else:
            check = mydic[thing].cget("text")
        if current == "":
            current = check
        elif current != check:
            return "  "

    return current


def checkforblank(mydic):
    for thing in mydic:
        if isinstance(mydic[thing], dict):
            check = checkforblank(mydic[thing])
            if check == True:
                return True
        else:
            check = mydic[thing].cget("text")
            if check == "  ":
                return True
    return False


def setall(mydic, mytype):
    for thing in mydic:
        if isinstance(mydic[thing], dict):
            setall(mydic[thing], mytype)
        else:
            mydic[thing].config(text=mytype)


def checkwin(path):
    won = False
    winner = "O"
    if len(path) == 1:
        while winner != " " and won == False:
            winconds = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for w in winconds:
                if (checkall(allbuttons[path[0]][w[0]]) == winner and
                        checkall(allbuttons[path[0]][w[1]]) == winner and
                        checkall(allbuttons[path[0]][w[2]]) == winner):
                    won = True
                    break
            if won: break
            if winner == "O":
                winner = "X"
            else:
                winner = " "

        if winner == "X" or winner == "O":
            if winner=="X":
                pattern=["X", " ", "X", " ", "X", " ", "X", " ", "X"]
                mycolour="red"
            if winner=="O":
                pattern=[" ", "O", " ", "O", " ", "O", " ", "O", " "]
                mycolour="blue"
            i = 0
            for w in pattern:
                if w == winner:
                    for square in allbuttons[path[0]][i]:
                        allbuttons[path[0]][i][square].config(highlightbackground=mycolour, bg=mycolour)
                        allcolours[path[0]][i][square]=mycolour
                else:
                    for square in allbuttons[path[0]][i]:
                        allbuttons[path[0]][i][square].config(highlightbackground="white", bg="white")
                        allcolours[path[0]][i][square] = "white"
                setall(allbuttons[path[0]][i], winner)
                i += 1

        elif winner == " ":
            if checkforblank(allbuttons[path[0]]) == False:
                for i in allbuttons[path[0]]:
                    for square in allbuttons[path[0]][i]:
                        allbuttons[path[0]][i][square].config(highlightbackground="yellow",bg="yellow")
                        allcolours[path[0]][i][square] = "yellow"
                setall(allbuttons[path[0]], "--")

    elif len(path) == 2:
        while winner != " " and won == False:
            winconds = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for w in winconds:
                if (allbuttons[path[0]][path[1]][w[0]].cget("text") == winner and allbuttons[path[0]][path[1]][
                        w[1]].cget("text") == winner and allbuttons[path[0]][path[1]][w[2]].cget("text") == winner):
                    won = True
                    break
            if won == True: break
            if winner == "O":
                winner = "X"
            else:
                winner = " "

        if winner == "X" or winner == "O":
            if winner=="X":
                pattern=["X", " ", "X", " ", "X", " ", "X", " ", "X"]
                mycolour="red"
            if winner=="O":
                pattern=[" ", "O", " ", "O", " ", "O", " ", "O", " "]
                mycolour="blue"

            i = 0
            for w in pattern:
                if w == winner:
                    allbuttons[path[0]][path[1]][i].config(highlightbackground=mycolour, bg=mycolour)
                    allcolours[path[0]][path[1]][i] = mycolour
                allbuttons[path[0]][path[1]][i].config(text=winner)
                i += 1

        elif winner == " ":
            if checkforblank(allbuttons[path[0]][path[1]]) == False:
                for square in allbuttons[path[0]][path[1]]:
                    allbuttons[path[0]][path[1]][square].config(highlightbackground="yellow", bg="yellow")
                    allcolours[path[0]][path[1]][square] = "yellow"
                setall(allbuttons[path[0]][path[1]], "--")


def domove(placement,iscomp=False):
    global allowed
    global turn
    print(turn)
    if (len(allowed) == 0 or
            (len(allowed) == 1 and placement[0] == allowed[0]) or
            (len(allowed) == 2 and placement[0] == allowed[0] and placement[1] == allowed[1])):

        if (isinstance(allbuttons[placement[0]], dict) and isinstance(allbuttons[placement[0]][placement[1]], dict) and
                allbuttons[placement[0]][placement[1]][placement[2]].cget("text") == "  "):

            allbuttons[placement[0]][placement[1]][placement[2]].config(text=turn)
            if turn == "X":
                turn = "O"
            else:
                turn = "X"

            if len(allowed) == 0:
                for mega in allbuttons:
                    for square in allbuttons[mega]:
                        if checkall(allbuttons[mega][square]) == "  ":
                            for button in allbuttons[mega][square]:
                                allbuttons[mega][square][button].config(highlightbackground="white",bg="white")
                                allcolours[mega][square][button] = "white"
                            checkwin([mega, square])
                        checkwin([mega])

            elif len(allowed) == 1:
                for square in allbuttons[allowed[0]]:
                    if checkall(allbuttons[allowed[0]][square]) == "  ":
                        for button in allbuttons[allowed[0]][square]:
                            allbuttons[allowed[0]][square][button].config(highlightbackground="white",bg="white")
                            allcolours[allowed[0]][square][button] = "white"

                for square in allbuttons[placement[0]]:
                    checkwin([placement[0], square])
                checkwin([placement[0]])

            elif len(allowed) == 2:
                for button in allbuttons[allowed[0]][allowed[1]]:
                    allbuttons[allowed[0]][allowed[1]][button].config(highlightbackground="white",bg="white")
                    allcolours[allowed[0]][allowed[1]][button] = "white"

                checkwin([placement[0], placement[1]])
                checkwin([placement[0]])

            allowed = [placement[1], placement[2]]

            if checkall(allbuttons[allowed[0]][allowed[1]]) != "  ":
                allowed.pop(1)

            if checkall(allbuttons[allowed[0]]) != "  ":
                allowed.pop(0)

            if len(allowed) == 0:
                for mega in allbuttons:
                    for square in allbuttons[mega]:
                        if checkall(allbuttons[mega][square]) == "  ":
                            for button in allbuttons[mega][square]:
                                allbuttons[mega][square][button].config(highlightbackground="green",bg="green")
                                allcolours[mega][square][button]="green"

            elif len(allowed) == 1:
                for square in allbuttons[allowed[0]]:
                    if checkall(allbuttons[allowed[0]][square]) == "  ":
                        for button in allbuttons[allowed[0]][square]:
                            allbuttons[allowed[0]][square][button].config(highlightbackground="green",bg="green")
                            allcolours[allowed[0]][square][button] = "green"

            elif len(allowed) == 2:
                for button in allbuttons[allowed[0]][allowed[1]]:
                    allbuttons[allowed[0]][allowed[1]][button].config(highlightbackground="green",bg="green")
                    allcolours[allowed[0]][allowed[1]][button] = "green"
            # if(iscomp==False):
            #     CPUmove()

def makewindow(upperD):
    mybuttons = {}
    r = 0
    for direction in intD:

        c = 0
        for newD in intD:
            mydir = 3 * int(direction / 3) + int(newD / 3)
            mynewD = (direction % 3) * 3 + newD % 3
            if mydir not in mybuttons:
                mybuttons[mydir] = {}

            mybuttons[mydir][mynewD] = Button(win, text="  ", font=("Helvetica", 10),
                                              highlightbackground="green", bg="green",
                                              command=lambda k=[upperD, mydir, mynewD]: domove(k))
            mybuttons[mydir][mynewD].bind("<Enter>", on_enter)
            mybuttons[mydir][mynewD].bind("<Leave>", on_leave)
            mybuttons[mydir][mynewD].grid(row=r, column=c)
            if c % 4 == 2:
                c += 1
                wall = Label(win, text=" ", font=("Helvetica", 1), bg="gray")
                wall.grid(row=r, column=c)
            c += 1
        if r % 4 == 2:
            r += 1
            wall = Label(win, text=" ", font=("Helvetica", 1), bg="gray")
            wall.grid(row=r, column=0)
        r += 1
    return mybuttons

def CPUmove():
    mypick=[4,4,random.randint(3,5)]
    if len(allowed)>=1:
        mypick[0]=allowed[0]
    if len(allowed)>=2:
        mypick[1]=allowed[1]
    print(mypick)

    if len(allowed)==2:
        mymoves=[]
        for button in allbuttons[mypick[0]][mypick[1]]:
            mymoves.append(allbuttons[mypick[0]][mypick[1]][button].cget("text"))

        mypick[2]=evalmoves(mymoves,turn)[0]

    if len(allowed)==1:
        bestscore=[]
        for potmove in intD:
            mymoves=[]
            for button in allbuttons[mypick[0]][potmove]:
                mymoves.append(allbuttons[mypick[0]][potmove][button].cget("text"))

            temp=evalmoves(mymoves,turn)
            if bestscore==[] or temp[1]>=bestscore[1]:
                bestscore=[temp[0],temp[1],potmove]
        print("best:",bestscore)

        mypick[1] = bestscore[2]
        mypick[2] = bestscore[0]


    if allbuttons[mypick[0]][mypick[1]][mypick[2]].cget("text")=="  ":
        domove(mypick,True)
    else:
        print("DIDNT WORK!!!!",mypick)

def evalmoves(myboard,player):
    movestr=[0,-1]
    for i in intD:
        if myboard[i] == "  ":
            movestr = [i,0]
            break
    if player == "X":
        opp="O"
    else:
        opp="X"

    lines=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    #your moves limited
    for youwin in lines:
        if myboard[youwin[1]] == "  " and myboard[youwin[0]] == player and myboard[youwin[2]] == "  ": movestr = [
            youwin[2], 2]
        if myboard[youwin[2]] == "  " and myboard[youwin[1]] == player and myboard[youwin[0]] == "  ": movestr = [
            youwin[0], 2]
        if myboard[youwin[0]] == "  " and myboard[youwin[2]] == player and myboard[youwin[1]] == "  ": movestr = [
            youwin[1], 2]

    #your moves
    for youwin in lines:
        if myboard[youwin[0]]==player and myboard[youwin[1]]==player and myboard[youwin[2]]=="  ": movestr=[youwin[2],2]
        if myboard[youwin[2]]==player and myboard[youwin[1]]==player and myboard[youwin[0]]=="  ": movestr=[youwin[0],2]
        if myboard[youwin[0]]==player and myboard[youwin[2]]==player and myboard[youwin[1]]=="  ": movestr=[youwin[1],2]

    #enemy moves
    for youwin in lines:
        if myboard[youwin[0]]==opp and myboard[youwin[1]]==opp and myboard[youwin[2]]=="  ": movestr=[youwin[2],3]
        if myboard[youwin[2]]==opp and myboard[youwin[1]]==opp and myboard[youwin[0]]=="  ": movestr=[youwin[0],3]
        if myboard[youwin[0]]==opp and myboard[youwin[2]]==opp and myboard[youwin[1]]=="  ": movestr=[youwin[1],3]

    return(movestr)

myboard=[
    "  ","  ","O",
    "X","  ","  ",
    "O","  ","  "]
print(evalmoves(myboard,"X"))

allbuttons = {}
allcolours = {}
for direction in intD:
    allcolours[direction]={}
    for game in intD:
        allcolours[direction][game] = {}
        for square in intD:
            allcolours[direction][game][square] = "green"

r = 0
c = 0
width = 400
height = 240
for direction in intD:
    win = Tk()
    win.config(bg="gray")
    allbuttons[direction] = makewindow(direction)
    win.geometry(f"{width}x{height}+{r * width + 20}+{c * height +c*30+ 20}")
    r += 1
    if r == 3:
        c += 1
        r = 0

win.mainloop()

from tkinter import *
import copy

intD=[
    0,1,2,
    3,4,5,
    6,7,8,]

allowed=[]
turn="X"

stypes=["X","O","  "]

def checkall(mydic):
    current=""
    check = ""
    for thing in mydic:
        if isinstance(mydic[thing],dict):
            check=checkall(mydic[thing])
        else:
            check=mydic[thing].cget("text")
        if current=="":
            current=check
        elif current!=check:
            return "  "
    return current

def setall(mydic,type):
    for thing in mydic:
        if isinstance(mydic[thing],dict):
            setall(mydic[thing],type)
        else:
            mydic[thing].config(text=type)

def checkwin(path):
    won=False
    winner="O"
    print("pathlen ",len(path))
    if (len(path) == 1):
        while winner != " " and won == False:
            winconds = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for w in winconds:
                if (checkall(allbuttons[path[0]][w[0]]) == winner and
                        checkall(allbuttons[path[0]][w[1]]) == winner and
                        checkall(allbuttons[path[0]][w[2]]) == winner):
                    won = True
                    break
            if won == True: break
            if winner == "O":
                winner = "X"
            else:
                winner = " "
        #print("winner:", winner)
        if (winner == "X"):
            i = 0
            for w in ["X", " ", "X", " ", "X", " ", "X", " ", "X"]:
                if w == "X":
                    for square in allbuttons[path[0]][i]:
                        allbuttons[path[0]][i][square].config(highlightbackground="red")
                else:
                    for square in allbuttons[path[0]][i]:
                        allbuttons[path[0]][i][square].config(highlightbackground="white")
                setall(allbuttons[path[0]][i],"X")
                i += 1
            #allbuttons[path[0]][path[1]] = "X"
        if (winner == "O"):
            i = 0
            for w in [" ", "O", " ", "O", " ", "O", " ", "O", " "]:
                if w == "O":
                    for square in allbuttons[path[0]][i]:
                        allbuttons[path[0]][i][square].config(highlightbackground="blue")
                else:
                    for square in allbuttons[path[0]][i]:
                        allbuttons[path[0]][i][square].config(highlightbackground="white")
                setall(allbuttons[path[0]][i], "O")
                i += 1
            #allbuttons[path[0]][path[1]] = "O"


    if(len(path)==2):
        while winner!=" " and won==False:
            winconds=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
            for w in winconds:
                if (allbuttons[path[0]][path[1]][w[0]].cget("text")==winner and allbuttons[path[0]][path[1]][w[1]].cget("text")==winner and allbuttons[path[0]][path[1]][w[2]].cget("text")==winner):
                    won=True
                    break
            if won==True: break
            if winner=="O": winner="X"
            else: winner=" "
        #print("winner:",winner)
        if(winner=="X"):
            i=0
            for w in ["X"," ","X"," ","X"," ","X"," ","X"]:
                if w=="X":
                    allbuttons[path[0]][path[1]][i].config(highlightbackground="red")
                allbuttons[path[0]][path[1]][i].config(text="X")
                i+=1
            #allbuttons[path[0]][path[1]]="X"
        if (winner == "O"):
            i=0
            for w in [" ", "O", " ", "O", " ", "O", " ", "O", " "]:
                if w == "O":
                    allbuttons[path[0]][path[1]][i].config(highlightbackground="blue")
                allbuttons[path[0]][path[1]][i].config(text="O")
                i+=1
            #allbuttons[path[0]][path[1]] = "O"


def domove(placement):
    global allowed
    global turn
    if (len(allowed)==0 or
        (len(allowed)==1 and placement[0]==allowed[0]) or
        (len(allowed)==2 and placement[0]==allowed[0]and placement[1]==allowed[1])):
        if(isinstance(allbuttons[placement[0]],dict) and isinstance(allbuttons[placement[0]][placement[1]],dict) and
                allbuttons[placement[0]][placement[1]][placement[2]].cget("text")=="  "):
            allbuttons[placement[0]][placement[1]][placement[2]].config(text=turn)
            if turn=="X": turn="O"
            else: turn="X"

            if len(allowed) == 0:
                for mega in allbuttons:
                    for square in allbuttons[mega]:
                        if checkall(allbuttons[mega][square]) == "  ":
                            for button in allbuttons[mega][square]:
                                allbuttons[mega][square][button].config(highlightbackground="white")
                            checkwin([mega, square])
                        checkwin([mega])

            if len(allowed) == 1:
                for square in allbuttons[allowed[0]]:
                    if checkall(allbuttons[allowed[0]][square])=="  ":
                        for button in allbuttons[allowed[0]][square]:
                            allbuttons[allowed[0]][square][button].config(highlightbackground="white")

                for square in allbuttons[placement[0]]:
                    checkwin([placement[0],square])
                checkwin([placement[0]])


            if len(allowed) == 2:
                for button in allbuttons[allowed[0]][allowed[1]]:
                    allbuttons[allowed[0]][allowed[1]][button].config(highlightbackground="white")

                checkwin([placement[0],placement[1]])
                checkwin([placement[0]])

            allowed=[placement[1],placement[2]]

            #print("allowed 1: ",allowed[1])
            print("checked [",checkall(allbuttons[allowed[0]][allowed[1]]),"]")
            if checkall(allbuttons[allowed[0]][allowed[1]])=="X" or checkall(allbuttons[allowed[0]][allowed[1]])=="O":
                allowed.pop(1)
                #print("popped list")
            if checkall(allbuttons[allowed[0]])=="X" or checkall(allbuttons[allowed[0]])=="O":
                allowed.pop(0)

            if len(allowed) == 0:
                for mega in allbuttons:
                    for square in allbuttons[mega]:
                        if checkall(allbuttons[mega][square])=="  ":
                            for button in allbuttons[mega][square]:
                                allbuttons[mega][square][button].config(highlightbackground="green")

            if len(allowed) == 1:
                for square in allbuttons[allowed[0]]:
                    if checkall(allbuttons[allowed[0]][square])=="  ":
                        for button in allbuttons[allowed[0]][square]:
                            allbuttons[allowed[0]][square][button].config(highlightbackground="green")

            if len(allowed)==2:
                for button in allbuttons[allowed[0]][allowed[1]]:
                    allbuttons[allowed[0]][allowed[1]][button].config(highlightbackground="green")



        #print(allbuttons[allowed[0]][allowed[1]])

def makewindow(upperD):
    mybuttons = {}
    r = 0
    for direction in intD:

        c = 0
        for newD in intD:
            mydir=3*int(direction/3)+int(newD/3)
            mynewD=(direction%3)*3+newD%3
            if mydir not in mybuttons:
                mybuttons[mydir] = {}
            mybuttons[mydir][mynewD] = Button(win, text="  ", font=("Helvetica", 10),
                                                highlightbackground="white",
                                                command=lambda k=[upperD, mydir, mynewD]: domove(k))
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

allbuttons={}
r=0
c=0
width=400
height=240
for direction in intD:
    win=Tk()
    win.config(bg="gray")
    allbuttons[direction]=makewindow(direction)
    win.geometry(f"{width}x{height}+{r*width+r*20}+{c*height+c*40}")
    r+=1
    if(r==3):
        c+=1
        r=0

print(allbuttons)

win.mainloop()
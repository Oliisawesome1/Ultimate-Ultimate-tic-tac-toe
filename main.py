import copy
import time
global totalends
import random



# your code here

#0
#1
#2
#3
#4        K
#5
#6
#7        R
#8
#totalends=0
# 0 1 2 3 4 5 6 7 8
checkmate=input("try to stop stalemates? (doesnt work correctly) y/n ")
maxrand=int(input("max rand of not moving: "))
if checkmate == "y": checkmate = True
else: checkmate = False

makeboardavg=[]
fullavg=[]
findmovesavg=[]

def printboard(moves):
    i = 0
    n = 0
    print("rc 0   1   2   3   4   5   6   7")
    thisboard = makeboard(moves)
    while i < len(thisboard):
        p = 0
        print(n, "", end="")
        n = n + 1
        while p < len(thisboard[i]):
            if (str(i) + str(p) == moves[len(moves) - 1][0] + moves[len(moves) - 1][1]):
                print("-" + thisboard[i][p] + "-", end="")
            elif (str(i) + str(p) == moves[len(moves) - 1][2] + moves[len(moves) - 1][3]):
                print("!" + thisboard[i][p] + "!", end="")
            else:
                # if (i+p)%2==0:
                #     print("{" + thisboard[i][p] + "}", end="")
                # else:
                    print("[" + thisboard[i][p] + "]", end="")
            p = p + 1
        i = i + 1
        print("")

def makeboard(mymovehist):
    start = time.process_time()
    simboard=[
        ["BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"],
        ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
        ["WR", "WH", "WB", "WQ", "WK", "WB", "WH", "WR"]]
    # simboard = [
    #     ["  ", "  ", "  ", "  ", "BK", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "BP"],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "BQ", "WK", "  ", "  ", "  "]]

    # simboard=[
    #     ["BR", "  ", "BB", "BQ", "  ", "BR", "  ", "BK"],
    #     ["BP", "  ", "BP", "BP", "  ", "BP", "BP", "  "],
    #     ["  ", "BP", "BH", "  ", "  ", "BH", "  ", "BP"],
    #     ["  ", "  ", "  ", "  ", "BP", "  ", "  ", "  "],
    #     ["WP", "  ", "WB", "BB", "WP", "  ", "WP", "WP"],
    #     ["  ", "  ", "WH", "  ", "  ", "WH", "  ", "  "],
    #     ["  ", "WP", "WP", "WP", "  ", "WP", "  ", "  "],
    #     ["  ", "WR", "WB", "WQ", "WK", "WR", "  ", "  "]]
    # simboard = [
    #     ["BR", "BH", "BB", "BQ", "BK", "  ", "  ", "  "],
    #     ["BP", "BP", "BP", "BP", "BB", "BP", "BP", "BR"],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "BH"],
    #     ["  ", "  ", "  ", "  ", "  ", "WP", "  ", "WP"],
    #     ["  ", "  ", "  ", "  ", "WQ", "WH", "  ", "  "],
    #     ["WP", "WP", "WP", "  ", "WP", "  ", "  ", "  "],
    #     ["WR", "WH", "WB", "  ", "WK", "WB", "  ", "WR"]]
    # simboard = [
    #     ["BK", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "WR", "  ", "  ", "  ", "  "],
    #     ["WP", "  ", "  ", "WQ", "WH", "  ", "  ", "  "],
    #     ["  ", "BP", "BP", "  ", "WP", "  ", "  ", "  "],
    #     ["  ", "WP", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "WH", "  ", "WP", "  ", "  ", "  "],
    #     ["WP", "  ", "WP", "  ", "  ", "  ", "  ", "  "],
    #     ["WR", "  ", "WB", "  ", "WK", "  ", "  ", "  "]]
    # simboard = [
    #     ["BK", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "WR", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "WR", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    #     ["  ", "  ", "  ", "  ", "WK", "  ", "  ", "  "]]
    for i in mymovehist:
        # if simboard[int(i[2])][int(i[3])]=="BK" or simboard[int(i[2])][int(i[3])] == "WK":
        #     simboard[int(i[2])][int(i[3])] = copy.copy(simboard[int(i[0])][int(i[1])])
        #     simboard[int(i[0])][int(i[1])] = "  "
        #     #print("predicted checkmate")
        #     break
        simboard[int(i[2])][int(i[3])] = copy.copy(simboard[int(i[0])][int(i[1])])
        if int(i[2])==0 and simboard[int(i[2])][int(i[3])]=="WP":
            simboard[int(i[2])][int(i[3])] = "WQ"
        elif int(i[2])==7 and simboard[int(i[2])][int(i[3])]=="BP":
            simboard[int(i[2])][int(i[3])] = "BQ"
        #print(simboard[int(i[2])][int(i[3])],int(i[2]),int(i[3]))
        simboard[int(i[0])][int(i[1])] = "  "
    # r=0
    # while r<8:
    #     c=0
    #     while c<7:
    #         if simboard[r][c]=="BK":
    #             positions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    #             for position in positions:
    #                 if r + position[0] <= 7 and r + position[0] >= 0 and c + position[1] <= 7 and c + position[1] >= 0 and simboard[r + position[0]][c + position[1]].upper()[0] == ' ':
    #                     simboard[r+position[0]][c+position[1]]=" B"
    #         if simboard[r][c]=="WK":
    #             positions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    #             for position in positions:
    #                 if r + position[0] <= 7 and r + position[0] >= 0 and c + position[1] <= 7 and c + position[1] >= 0 and simboard[r + position[0]][c + position[1]].upper()[0] == ' ':
    #                     if simboard[r+position[0]][c+position[1]]==" B":
    #                         simboard[r + position[0]][c + position[1]] = "  "
    #                     else: simboard[r+position[0]][c+position[1]]=" W"
    #         c+=1
    #     r+=1
    makeboardavg.append(time.process_time()-start)
    return simboard

def findmoves(boardref,player):
    r=0
    newmoves=[]
    start = time.process_time()
    while r<8:
        c=0
        while c<8:
            pos = str(r) + str(c)

            #white
            if boardref[r][c]!="  ":
                if boardref[r][c].upper()=="WP":
                    if r-1>=0 and boardref[r-1][c][0]==' ':
                        if player==0:
                            if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos+str(r-1)+str(c))
                    if r==6 and boardref[r-1][c][0]==' ' and boardref[r-2][c][0]==' ':
                        if player==0:
                            if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos+str(r-2)+str(c))
                    if r-1>=0 and c>0 and boardref[r-1][c-1].upper()[0]=='B':
                        if player==0:
                            if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos+str(r-1)+str(c-1))
                    if r-1>=0 and c>0 and boardref[r-1][c-1]==" B":
                        boardref[r-1][c-1]="  "

                    if r-1>=0 and c<7 and boardref[r-1][c+1].upper()[0]=='B':
                        if player==0:
                            if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos+str(r-1)+str(c+1))
                    if r-1>=0 and c<7 and boardref[r-1][c+1]==" B":
                        boardref[r-1][c+1]="  "
                    if r-1>=0 and c>0 and boardref[r-1][c-1][0]=='W':
                        boardref[r-1][c-1]='w'+boardref[r-1][c-1][1]
                    if r-1>=0 and c<7 and boardref[r-1][c+1][0]=='W':
                        boardref[r-1][c+1]='w'+boardref[r-1][c+1][1]
                elif boardref[r][c].upper() == "WH":
                    positions=[[2,1],[-2,1],[2,-1],[-2,-1], [1,2],[1,-2],[-1,2],[-1,-2]]
                    for position in positions:
                        if r+position[0] <= 7 and r+position[0] >= 0 and c+position[1] <= 7 and c+position[1] >= 0 and boardref[r+position[0]][c+position[1]].upper()[0]!='W':
                            if player==0:
                                if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + position[0]) + str(c + position[1]))
                            if boardref[r + position[0]][c + position[1]] == " B":
                                boardref[r + position[0]][c + position[1]] = "  "
                            if boardref[r + position[0]][c + position[1]][0] == 'W':
                                boardref[r + position[0]][c + position[1]] = 'w'+boardref[r + position[0]][c + position[1]][1]

                if boardref[r][c].upper() == "WR" or boardref[r][c].upper() == "WQ":
                    ipos = 0
                    while ipos < 4:
                        num = 1
                        while True:
                            poss = [[0, -num], [0, num], [num, 0], [-num, 0]]
                            if r + poss[ipos][0] <= 7 and r + poss[ipos][0] >= 0 and c + poss[ipos][1] <= 7 and c + \
                                    poss[ipos][1] >= 0:
                                if boardref[r + poss[ipos][0]][c + poss[ipos][1]].upper()[0] == 'B':
                                    if player==0:
                                        if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + poss[ipos][0]) + str(c + poss[ipos][1]))
                                    boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "b" + boardref[r + poss[ipos][0]][
                                        c + poss[ipos][1]][1]
                                    break
                                elif boardref[r + poss[ipos][0]][c + poss[ipos][1]].upper()[0] == 'W':
                                    boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "w" + boardref[r + poss[ipos][0]][
                                        c + poss[ipos][1]][1]
                                    break
                                else:
                                    if player==0:
                                        if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + poss[ipos][0]) + str(c + poss[ipos][1]))
                                    if boardref[r + poss[ipos][0]][c + poss[ipos][1]] == " B":
                                        boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "  "
                            else:
                                break
                            num = num + 1
                        ipos = ipos + 1
                if boardref[r][c].upper() == "WB" or boardref[r][c].upper() == "WQ":
                    ipos = 0
                    while ipos < 4:
                        num = 1
                        while True:
                            poss = [[num, num], [-num, num], [num, -num], [-num, -num]]
                            if r + poss[ipos][0] <= 7 and r + poss[ipos][0] >= 0 and c + poss[ipos][1] <= 7 and c + \
                                    poss[ipos][1] >= 0:
                                if boardref[r + poss[ipos][0]][c + poss[ipos][1]].upper()[0] == 'B':
                                    if player==0:
                                        if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + poss[ipos][0]) + str(c + poss[ipos][1]))
                                    boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "b" + boardref[r + poss[ipos][0]][
                                        c + poss[ipos][1]][1]
                                    break
                                elif boardref[r + poss[ipos][0]][c + poss[ipos][1]].upper()[0] == 'W':
                                    boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "w" + boardref[r + poss[ipos][0]][
                                        c + poss[ipos][1]][1]
                                    break
                                else:
                                    if player==0:
                                        if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + poss[ipos][0]) + str(c + poss[ipos][1]))
                                    if boardref[r + poss[ipos][0]][c + poss[ipos][1]] == " B":
                                        boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "  "
                            else:
                                break
                            num = num + 1
                        ipos = ipos + 1


                #black
                if boardref[r][c].upper()=="BP":
                    if r+1<=7 and boardref[r+1][c][0]==' ':
                        if player==1:
                            if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos+str(r+1)+str(c))
                    if r==1 and boardref[r+1][c][0]==' ' and boardref[r+2][c][0]==' ':
                        if player==1:
                            if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos+str(r+2)+str(c))
                    if r+1<=7 and c>0 and boardref[r+1][c-1].upper()[0]=='W':
                        if player==1:
                            if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos+str(r+1)+str(c-1))
                    if r+1<=7 and c>0 and boardref[r+1][c-1]==" W":
                        boardref[r+1][c-1]="  "
                    if r+1<=7 and c<7 and boardref[r+1][c+1].upper()[0]=='W':
                        if player==1:
                            if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos+str(r+1)+str(c+1))
                    if r+1<=7 and c<7 and boardref[r+1][c+1]==" W":
                        boardref[r+1][c+1]="  "
                    if r+1<=7 and c>0 and boardref[r+1][c-1][0]=='B':
                        boardref[r+1][c-1]='b'+boardref[r+1][c-1][1]
                    if r+1<=7 and c<7 and boardref[r+1][c+1][0]=='B':
                        boardref[r+1][c+1]='b'+boardref[r+1][c+1][1]
                elif boardref[r][c].upper() == "BH":
                    positions=[[-2,1],[2,1],[-2,-1],[2,-1], [1,2],[1,-2],[-1,2],[-1,-2]]
                    for position in positions:
                        if r+position[0] <= 7 and r+position[0] >= 0 and c+position[1] <= 7 and c+position[1] >= 0 and boardref[r+position[0]][c+position[1]].upper()[0]!='B':
                            if player==1:
                                if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + position[0]) + str(c + position[1]))
                            if boardref[r + position[0]][c + position[1]] == " W":
                                boardref[r + position[0]][c + position[1]] = "  "
                            if boardref[r + position[0]][c + position[1]][0] == 'B':
                                boardref[r + position[0]][c + position[1]] = 'b'+boardref[r + position[0]][c + position[1]][1]

                if boardref[r][c].upper() == "BR" or boardref[r][c].upper() == "BQ":
                    ipos = 0
                    while ipos < 4:
                        num = 1
                        while True:
                            poss = [[num, 0], [-num, 0], [0, -num], [0, num]]
                            if r + poss[ipos][0] <= 7 and r + poss[ipos][0] >= 0 and c + poss[ipos][1] <= 7 and c + poss[ipos][1] >= 0:
                                if boardref[r + poss[ipos][0]][c + poss[ipos][1]].upper()[0] == 'W':
                                    boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "w" + boardref[r + poss[ipos][0]][
                                        c + poss[ipos][1]][1]
                                    if player==1:
                                        if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + poss[ipos][0]) + str(c + poss[ipos][1]))
                                    break
                                elif boardref[r + poss[ipos][0]][c + poss[ipos][1]].upper()[0] == 'B':
                                    boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "b" + boardref[r + poss[ipos][0]][
                                        c + poss[ipos][1]][1]
                                    break
                                else:
                                    if player==1:
                                        if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + poss[ipos][0]) + str(c + poss[ipos][1]))
                                    if boardref[r + poss[ipos][0]][c + poss[ipos][1]] == " W":
                                        boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "  "
                            else:
                                break
                            num = num + 1
                        ipos = ipos + 1
                if boardref[r][c].upper() == "BB" or boardref[r][c].upper() == "BQ":
                    ipos = 0

                    while ipos<4:
                        num = 1
                        while True:
                            poss = [[num, num], [-num, num], [num, -num], [-num, -num]]
                            if 7 >= r + poss[ipos][0] >= 0 and 7 >= c + poss[ipos][1] >= 0:
                                if boardref[r+poss[ipos][0]][c+poss[ipos][1]].upper()[0]=='W':
                                    boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "w"+boardref[r + poss[ipos][0]][c + poss[ipos][1]][1]
                                    if player==1:
                                        if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + poss[ipos][0]) + str(c + poss[ipos][1]))
                                    break
                                elif boardref[r+poss[ipos][0]][c+poss[ipos][1]].upper()[0]=='B':
                                    boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "b" + boardref[r + poss[ipos][0]][
                                        c + poss[ipos][1]][1]
                                    break
                                else:
                                    if player==1:
                                        if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r + poss[ipos][0]) + str(c + poss[ipos][1]))
                                    if boardref[r + poss[ipos][0]][c + poss[ipos][1]] == " W":
                                        boardref[r + poss[ipos][0]][c + poss[ipos][1]] = "  "
                            else:
                                break
                            num=num+1
                        ipos=ipos+1
            c=c+1
        r=r+1
    r=0
    while r<8:
        c=0
        while c<8:
            pos= str(r)+str(c)

            if player==1 and boardref[r][c].upper() == "BK":
                positions=[[1,0],[-1,0],[0,1],[0,-1], [1,1],[1,-1],[-1,1],[-1,-1]]
                for position in positions:

                    if r+position[0] <= 7 and r+position[0] >= 0 and c+position[1] <= 7 and c+position[1] >= 0 and ((checkmate==False and boardref[r+position[0]][c+position[1]].upper()[0]!='B')or(checkmate==True and (boardref[r+position[0]][c+position[1]]==" B" or boardref[r+position[0]][c+position[1]][0]=='W'))): #

                        if maxrand==0 or random.randint(0,maxrand)!=0:

                            newmoves.append(pos + str(r + position[0]) + str(c + position[1]))

                if checkmate==True and boardref[r][c] == "bK":
                    if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r) + str(c))

            elif player==0 and boardref[r][c].upper() == "WK":
                positions=[[1,0],[-1,0],[0,1],[0,-1], [1,1],[1,-1],[-1,1],[-1,-1]]
                for position in positions:

                    if r+position[0] <= 7 and r+position[0] >= 0 and c+position[1] <= 7 and c+position[1] >= 0 and ((checkmate==False and boardref[r+position[0]][c+position[1]].upper()[0]!='W')or(checkmate==True and (boardref[r+position[0]][c+position[1]]==" W" or boardref[r+position[0]][c+position[1]][0]=='B'))): #

                        if maxrand==0 or random.randint(0,maxrand)!=0:

                            newmoves.append(pos + str(r + position[0]) + str(c + position[1]))

                if checkmate==True and boardref[r][c] == "wK":
                    if maxrand==0 or random.randint(0,maxrand)!=0: newmoves.append(pos + str(r) + str(c))

            c+=1
        r+=1

    findmovesavg.append(time.process_time()-start)
    return newmoves

def findscore(myboard):
    score=[0,0,0] # first is points negative is black winning. second is total pieces. third is middleness
    points={"BP":-1,"WP":1,"BR":-5,"WR":5,"BH":-3,"WH":3,"BB":-3,"WB":3,"BQ":-9,"WQ":9,"BK":-9999,"WK":9999}
    rn=0
    for r in myboard:
        rn+=1
        cn=0
        for c in r:
            cn+=1
            for p in points:
                if c==p:
                    score[0]+=points[p]
                    score[1]+=1
                    score[2]+=(4.5-abs((rn%7)-3.5))*(4.5-abs((cn%7)-3.5))
                    break
    # if score not in allscores :
    #     allscores.append(score)
    #     print(len(allscores))
    return score

def writemoves(thisboard,movehist,depth):
    start = time.process_time()
    myboard = makeboard(movehist)
    availmoves=findmoves(myboard,len(movehist)%2)
    #print(availmoves)
    if len(availmoves)==0:
        thisboard = 0
    #print(availmoves)
    howdone=0
    if (depth == botdepth):print("-"*len(availmoves),len(availmoves),"initial moves")
    for i in availmoves:

        if (depth == botdepth):
            howdone = howdone + 1
            #print(round(howdone / len(availmoves),2),end="")
            print("|", end="")
        thisboard[i] = {}
        newmovehist=copy.copy(movehist)
        newmovehist.append(i)
        if depth>0:
            writemoves(thisboard[i], newmovehist,depth-1)
        if depth==0:
            myboard=makeboard(newmovehist)
            # if len(findmoves(myboard, len(newmovehist) % 2))==0:
            #     thisboard[i] = [0,0,0]
            # else:
            global totalends
            totalends+=1
            thisboard[i] = findscore(myboard)
    fullavg.append(time.process_time() - start)

def pickmove(thisboard,player):

    score=[0,player*-10000,33,0]  # first is the move you pick, second is points, third is pieces
    for i in thisboard:
        if isinstance(thisboard[i],dict):
            opp=pickmove(thisboard[i],player*-1)

            if player==1 and opp[1]>score[1]:
                score= [i,opp[1],opp[2],opp[3]]
            elif player==-1 and opp[1]<score[1]:
                score= [i,opp[1],opp[2],opp[3]]
            elif opp[1]==score[1]:  # if score are same
                if opp[2]<score[2]:
                    score = [i,opp[1],opp[2],opp[3]]
                elif opp[2]==score[2] and opp[3]>score[3]:
                        score = [i, opp[1], opp[2], opp[3]]
                elif opp[2]==score[2] and opp[3]==score[3]:
                        score = [i, opp[1], opp[2], opp[3]]
        else:
            if player==1 and thisboard[i][0]>score[1]:
                score=[i,thisboard[i][0],thisboard[i][1],thisboard[i][2]]
            elif player==-1 and thisboard[i][0]<score[1]:
                score=[i,thisboard[i][0],thisboard[i][1],thisboard[i][2]]
            elif thisboard[i][0]==score[1]: # if value of both are same check next
                if thisboard[i][1]<score[2]:
                    score = [i,thisboard[i][0],thisboard[i][1],thisboard[i][2]]
                elif thisboard[i][1]==score[2] and thisboard[i][2]>score[3]:
                    score = [i, thisboard[i][0], thisboard[i][1], thisboard[i][2]]
                elif thisboard[i][1] == score[2] and thisboard[i][2] == score[3]:
                    score = [i, thisboard[i][0], thisboard[i][1], thisboard[i][2]]

    return score

moves=[]
side=1
youplay=input("you play? ")
botdepth=int(input("how many moves ahead? min 0 "))
board = {}

#writemoves(board,moves,0)
#print(board)
#print(findmoves(board,1))
totalends=0
while True:
    board = {}
    allscores = []
    if (side==1 and youplay=="y") or youplay!="y":
        if side == 1:
            print("finding moves for White. Progress:")

        else:
            print("finding moves for Black. Progress:")


        totalends=0

        writemoves(board,moves,botdepth)

        # for i in board:
        #     print(i, ":", pickmove(board[i], -1))
        print("",totalends,"end positions, picking a move")
        mymove=pickmove(board, side)
        print("MY MOVE THIS IS IT:",mymove)
        moves.append(mymove[0])
        print("expected result:",mymove[1],"points,",mymove[2],"total pieces,",mymove[3],"middleness")
        if moves[len(moves)-1] == 0:
            break
        print("full: ", 1000*sum(fullavg)/len(fullavg))
        print("finding: ", 1000*sum(findmovesavg) / len(findmovesavg))
        print("makeboard: ", 1000*sum(makeboardavg) / len(makeboardavg))
        print("\npast moves:", len(moves), moves, "\n")
        printboard(moves)

        print(findscore(makeboard(moves)))

    else:
        mymove=input("rcrc or undo: ")
        if(mymove=="undo"):
            moves.remove(moves[len(moves) - 1])
            moves.remove(moves[len(moves) - 1])
            moves.remove(moves[len(moves) - 1])
        else:
            moves.append(mymove)

        printboard(moves)
    if abs(findscore(makeboard(moves))[0]) > 900:
        break
    side = side*-1
if moves[len(moves)-1] == 0:
    print("draw :(")
elif findscore(makeboard(moves))[0] > 0:
    print("white wins!")
elif findscore(makeboard(moves))[0] < 0:
    print("black wins!")

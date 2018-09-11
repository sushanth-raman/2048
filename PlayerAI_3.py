from random import randint
from BaseAI_3 import BaseAI
import time
import math


class PlayerAI(BaseAI):
    def getMove(self, grid):
        self.startTime = time.clock()
        ran = grid.getAvailableMoves()
        self.maxdepth = 3
        moves = self.miniMax(grid,-float('inf'),float('inf'),self.maxdepth,True)
        print(self.maxdepth)
        if(grid.canMove([moves[0]])):
            return moves[0]
        else:
            return ran[randint(0,len(ran)-1)]




    def miniMax(self,grid,alpha,beta,depth,Max):
        if(depth == 0):
            return [None,self.eval(grid)]
        if(Max):
            possibleMoves = grid.getAvailableMoves()
            if(possibleMoves == []):
                return [None,self.eval(grid)]
            for move in possibleMoves:
                if (time.clock() - self.startTime > 0.18):
                    if(self.maxdepth > 1):
                        self.maxdepth = self.maxdepth - 1
                    break
                successor = grid.clone()
                successor.move(move)
                utility = self.miniMax(successor,alpha,beta,depth -1, False)
                if (utility[1] == -float('inf')):
                    self.moveChoice = move
                if (utility[1] > alpha):
                    self.moveChoice = move
                    alpha = utility[1]
                if (alpha >= beta):
                    break
            goalUtility = [self.moveChoice, alpha]
            return goalUtility

        else:
            possibleSpaces = grid.getAvailableCells()
            if (possibleSpaces == []):
                return [None, self.eval(grid)]

            for space in possibleSpaces:
                if (time.clock() - self.startTime > 0.18):
                    if(self.maxdepth > 1):
                        self.maxdepth = self.maxdepth - 1
                    break
                successor = grid.clone()
                successor.setCellValue(space,self.expectedTile())
                utility = self.miniMax(successor,alpha,beta,depth - 1,True)
                if (utility[1] < beta):
                    beta = utility[1]
                if (beta <= alpha):
                    break
            goalUtility = [self.moveChoice, beta]
            return goalUtility



    def eval(self,grid):
        heuristic2 = self.calcHeuristic2(grid)
        heuristic3 = self.calcHeuristic3(grid)
        heuristic4 = self.calcHeuristic4(grid)
        if heuristic4 != 0:
            heuristic4 = math.log2(heuristic4)
        #heuristic5 = self.calcHeuristic5(grid)
        heuristic6 = -1 * self.calcHeuristic6(grid)
        #if heuristic6 >= 1:
            #heuristic6 = -1 * math.log2(heuristic6)

                # heuristic 4 was 2.7 and 1 was 0.38 and 3 was 1.2 and 2 was 2.3
        # 3.3 * heuristic4

        # heuristics 1 was 0.54, heuristic 3 was 1.345, 2 was 2.89, 3.76 for 4 and 0.5 for 5, 0.65 = heuristic6. 0.
        #+ 1.43 * math.log2(heuristic5)

        #3 was 1.6 then 1.7, 4 was 4.3
        return 2.952*heuristic2 + 2.3*heuristic3 + 3.31 * heuristic4  + 0.81* heuristic6



    def calcHeuristic2(self,grid):
        heuristic2 = len(grid.getAvailableCells())
        return heuristic2

    def calcHeuristic3(self,grid):
        heuristic3 = 0

        for y in range(3,-1,-1):
            if(grid.getCellValue((y, 0)) >= grid.getCellValue((y, 1)) and grid.getCellValue((y, 1)) >= grid.getCellValue((y, 2)) and
                grid.getCellValue((y, 2)) >= grid.getCellValue((y, 3))):
                if(y==3):
                    #WAS 6.2
                    heuristic3 += 5.2
                if(y==2):
                    #Was 2.6
                    heuristic3 += 3.1
                if(y==1):
                    heuristic3 += 1.8
                if(y==0):
                    heuristic3 += 1
            else:
                if (y == 3):
                    #was 6.2
                    heuristic3 -= 5.2
                if (y == 2):
                    #was 2.6
                    heuristic3 -= 3.1
                if (y == 1):
                    #was 1.3
                    heuristic3 -= 1.8
                if (y == 0):
                    heuristic3 -= 1

        for x in range (0,4,1):
            if (grid.getCellValue((3, x)) >= grid.getCellValue((2, x)) and grid.getCellValue(
                    (2, x)) >= grid.getCellValue((1, x)) and grid.getCellValue((1, x)) >= grid.getCellValue((0, x))):
                if(x==0):
                    #was5.1
                    heuristic3 += 4.1
                if(x==1):
                    heuristic3 += 1.7

                if(x==2):
                    #wsa 1.3
                    heuristic3 += 1.5
                if(x==3):
                    heuristic3 += 1
            else:
                if(x == 0):
                    #was 5.1
                    heuristic3 -= 4.1

                if(x == 1):

                    heuristic3 -= 1.7

                if(x == 2):
                    #was 1.3
                    heuristic3 -= 1.5

                if(x == 3):
                    heuristic3 -= 1
        if(grid.getCellValue((3,0)) >= grid.getCellValue((2,1)) and grid.getCellValue((2,1)) >= grid.getCellValue((1,2))):
            heuristic3 += 2
        else:
            heuristic3 -= 2
        if (grid.getCellValue((3, 1)) >= grid.getCellValue((2, 2)) and grid.getCellValue((2, 2)) >= grid.getCellValue((1, 3))):
            heuristic3 += 0.8
        else:
            heuristic3 -= 0.8
        #if (grid.getCellValue((2, 0)) >= grid.getCellValue((1, 1))):
            #heuristic3 += 0.65
        #else:
           #heuristic3 -= 0.65

        return heuristic3





    def calcHeuristic4(self,grid):
        #was 1.35
        return 1*grid.getCellValue((3,0))# + 0.2 * grid.getCellValue((3,1))# + 0.06 * grid.getCellValue((3,2))
        #+ 0.138 * grid.getCellValue((2,0)) + 0.06 * grid.getCellValue((3,2))

    def calcHeuristic5(self,grid):
        return grid.getMaxTile()

    def calcHeuristic6(self,grid):
        heuristic6 = 0
        for x in range (0,4,1):
            for y in range(3,0,-1):
                if(y == 0 and x == 3):
                    heuristic6 += 0
                elif(x == 3):
                    if(grid.getCellValue((y,x)) > 0 and grid.getCellValue((y-1,x)) > 0 and abs(grid.getCellValue((y,x)) - grid.getCellValue((y-1,x))) > 0):
                        heuristic6 += math.log2(abs(grid.getCellValue((y,x)) - grid.getCellValue((y-1,x))))
                elif(y == 0):
                    if(grid.getCellValue((y,x)) > 0 and grid.getCellValue((y,x+1)) > 0 and abs(grid.getCellValue((y,x)) - grid.getCellValue((y,x+1))) > 0):
                        heuristic6 += math.log2(abs(grid.getCellValue((y,x)) - grid.getCellValue((y,x+1))))
                else:
                    if ( grid.getCellValue((y, x)) > 0 and grid.getCellValue((y-1, x)) > 0 and abs(grid.getCellValue((y,x)) - grid.getCellValue((y-1,x))) > 0):
                        heuristic6 += math.log2(abs(grid.getCellValue((y,x)) - grid.getCellValue((y-1,x))))
                    if (grid.getCellValue((y, x)) > 0 and grid.getCellValue((y, x+1)) > 0 and abs(grid.getCellValue((y,x)) - grid.getCellValue((y,x+1))) > 0):
                        heuristic6 += math.log2(abs(grid.getCellValue((y,x)) - grid.getCellValue((y,x+1))))
        return heuristic6


    def expectedTile(self):
        if randint(0,99) < 90:
            return 2
        else:
            return 4

    def __init__(self):
        self.moveChoice = None

    def calcAdjacent(self,x,y):
        adjacent = []
        if(y != 0):
            adjacent.append((x-1,y))
        if(x != 0):
            adjacent.append((y,x-1))
        return adjacent









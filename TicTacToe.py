import TTBoard as TTBoardSoln

def main():
    # create an empty board
    # this is the root of the tree
    doPointAdj = True
    doAlphaBeta = False

    TTBoardSoln.TTBoard.numboards = 0
    TTBoardSoln.TTBoard.numsearched = 0
    bd = TTBoardSoln.TTBoard(TTBoardSoln.XMOVE, pointAdj=doPointAdj)
    # create a board for every possible initial X move
    bd.createchildren()
    
    # Select alpha beta pruning or minimax
    if (doAlphaBeta):
        bd.alphabeta(-TTBoardSoln.HUGEVAL, TTBoardSoln.HUGEVAL, True)
    else:
        bd.minimax()
        
    bd.treetofile(depth=9)
    print('There are ', str(bd.numboards), ' boards; there were ', str(bd.numsearched), ' searched')

if __name__ == "__main__":
    main()
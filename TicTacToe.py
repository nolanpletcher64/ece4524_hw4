import TTBoardSoln

def main():
    # create an empty board
    # this is the root of the tree
    doPointAdj = True

    TTBoardSoln.TTBoard.numboards = 0
    TTBoardSoln.TTBoard.numsearched = 0
    bd = TTBoardSoln.TTBoard(TTBoardSoln.XMOVE, pointAdj=doPointAdj)
    # create a board for every possible initial X move
    bd.createchildren()
    bd.minimax()
    bd.treetofile(depth=9)
    print('There are ', str(bd.numboards), ' boards; there were ', str(bd.numsearched), ' searched')

if __name__ == "__main__":
    main()
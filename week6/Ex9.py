def printPair(open, close, out):
    if close == 0:
        return
    elif open == 0:
        print(out + close * ')')
    elif open == close:
        printPair(open-1,close,out + '(')
    else:
        printPair(open-1,close,out + '(')
        printPair(open,close-1,out + ')')

def pair(n):
    printPair(n,n,"")


    
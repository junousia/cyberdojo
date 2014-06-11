import sys

def printDiamond(start):
    width = (ord(start) - ord('A')) * 2 + 1
    for i in range (-(width/2), width/2 + 1):
        list = [' ' for j in range (-(width/2),width/2 + 1)]
        list[abs(i)] = chr(ord(start) - abs(i))
        list[-abs(i) - 1] = chr(ord(start) - abs(i))
        print "".join(list)

if __name__ == '__main__':
    if(len(sys.argv)) <= 1:
        printDiamond('Z')
    else:
        printDiamond(sys.argv[1][0]);

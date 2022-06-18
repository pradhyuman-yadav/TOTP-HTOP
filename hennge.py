import numpy as np

def main():
    cases(testcase=int(input()))
    
def cases(testcase:int):
    if(testcase < 1):
        return 0
    else:
        size = int(input())
        case(np.array(input().strip().split(), int))
        return (cases(testcase=(testcase-1)))

def case(arr):
    print (np.sum( np.power(list(filter(lambda x: (x >= 0), arr)), 2) ))



if __name__ == "__main__":
    main()
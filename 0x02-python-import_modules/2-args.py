#!/usr/bin/python3

if __name__ == "__main__":
    """ prints the command line arguments in an ordered manner """
    import sys

    args_sum = len(sys.argv) - 1
    if args_sum == 0:
        print("0 arguments.")
    elif args_sum == 1:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(args_sum))
        for i in range(args_sum):
            print("{}: {}".format(i + 1, sys.argv[i + 1]), end='\n')

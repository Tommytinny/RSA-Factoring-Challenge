#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def divid(number, factor):
        x = int(number / factor)
        return x

    arg = len(sys.argv)
    if arg < 2 or arg > 2:
        print("no file or more than one file passed")
        sys.exit()
        

    file = open(sys.argv[1], 'r')
    for line in file:
        number = int(line)
        factor1 = 2

        while factor1 * divid(number, factor1) != number:
            factor1 += 1

        factor2 = int(number / factor1)
        print("{}={}*{}".format(number, factor2, factor1))
    file.close

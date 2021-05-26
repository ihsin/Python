import sys
import getopt

def readLinebyLine():
    """readLinebyLine <-p> <File_path>"""
    path = ""
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hp:")
    except getopt.GetoptError:
        print("readLinebyLine <-p> <File_path>")
    for opt, arg in opts:
        if opt == '-h':
            print("")
        if opt == '-p':
            path = arg
    content = open(path, 'r')
    lines = content.readlines()
    #get lines in a list
    i = 0
    for line in lines:
        i = i + 1
        print("Line no {}: {} ".format(i, line))

    content.close()

readLinebyLine()
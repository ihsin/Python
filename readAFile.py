import getopt
import sys

def readAFile():
    """readAFile.py <-p> <File_path>"""
    argv = sys.argv[1:]
    path = ""
    try:
        opts, arg = getopt.getopt(argv, 'hp:')
    except getopt.GetoptError:
        print("readAFile.py <-p> <File_path>")
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print("readAFile.py <-p> <File_path>")
        if opt == '-p':
            path = arg
    if path != "":
        content = open(path)
        print(content.read())
    else:
        print("Must provide -p option")

readAFile()
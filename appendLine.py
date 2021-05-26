#Write a Python program to append text to a file and display the text.
import sys
import getopt

def appendLine():
    """appendLine.py [-h] [-p] [path_to_file]"""
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'hp:')
    except getopt.GetoptError:
        print("appendLine.py [-h] [-p] [path_to_file]")
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print("appendLine.py [-h] [-p] [path_to_file]")
        if opt == '-p':
            path = arg
            with open(path, 'a') as file:
                file.write("## Appended Line added ##")
            content = open(path)
            print(content.read())

appendLine()

            

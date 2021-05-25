import os
import sys
import getopt


def createFile():
	argv = sys.argv[1:]
	path = os.getenv('HOME')
	filename = os.path.basename(path) + '.txt'
	try:
		opts, args = getopt.getopt(argv, "hp:f:")
	except getopt.GetoptError:
		print("createFile.py -p <path> -f <filename>")
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-p':
			path = arg
		elif opt == '-h':
			print("createFile.py -p <path> -f <filename>")
		elif opt == '-f':
			filename = arg + ".txt"
	with open(os.path.join(path, filename), 'w'):
		pass
	print("Created file {} in {}".format(filename, path))

createFile()



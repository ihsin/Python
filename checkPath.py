import os
import sys
import getopt


def checkPath():
	"""checkPath.py -p <argument>"""
	argv = sys.argv[1:]
	path = os.getenv('HOME')
	try:
		opts, args = getopt.getopt(argv, "hp:")
	except getopt.GetoptError:
		print("checkPath.py -p <argument>")
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-h':
			print("checkPath.py -p <argument>")
			sys.exit()
		if opt == '-p':
			path = arg
	if os.path.exists(path):
		if os.path.isfile(path):
			print("Name of the file is {} and directory is {}".format(os.path.basename(path), os.path.dirname(path)))

checkPath()


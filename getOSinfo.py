# Write a Python program to get the name of the operating system (Platform independent), 
# information of current operating system, current working directory, 
# print files and directories in the current directory and 
# raises error in the case of invalid or inaccessible file names and paths.

import os
import platform
from datetime import datetime, timezone


print("OS name os : ", os.name)
print("OS information : ", os.uname())
print("Current Working Directory :", os.getcwd())
print("Files and Directories in current folder :", os.listdir('.'))

print("Platform : ", platform.system())
print("Platform release : ", platform.release())

#Write a Python program to list only directories, files and all directories, files in a specified path.

#listing only directories
path = os.getcwd()
print ("Listing Directories: ")
for name in os.listdir(path):
    if os.path.isdir(name):
        print (name)

#listing only files
print ("Listing Files: ")
for name in os.listdir(path):
    if os.path.isfile(name):
        print (name)     
        
#Write a Python program to get the size, permissions, owner, device, created, last modified and last accessed date time of a specified path.

stat_result = os.stat(path)
print (stat_result)

file_stat = os.stat(os.path.join(path, 'README.md'))

print ("printing size of file {} in bytes: {}".format(os.path.join(path, 'README.md'), file_stat.st_size))
# print (file_stat.st_size)
#shows in seconds counted from 1/1/1970
print (file_stat.st_mtime)
#convert 
print (datetime.fromtimestamp(stat_result.st_mtime, tz=timezone.utc))

#Write a Python program to create a symbolic link and read it to decide the original file pointed by the link.
path = '/tmp/' + os.path.basename(__file__)
print('Creating link {} -> {}'.format(path, __file__))
os.symlink(__file__, path)
stat_info = os.lstat(path)
print('\nFile Permissions:', oct(stat_info.st_mode))
print('\nPoints to:', os.readlink(path))
#removes the file path
os.unlink(path)


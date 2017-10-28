import sys
import re
import os
import random
import shutil


def walkdir(folder_address):
    i = 398
    folder_roots = [os.path.join(folder_address,f1) for f1 in os.listdir(folder_address)]
    for folder in folder_roots:
        child_folders = [os.path.join(folder,f2) for f2 in os.listdir(folder)]
        for child_folder in child_folders:
            files = [os.path.join(child_folder,f3) for f3 in os.listdir(child_folder)]
            for file in files:
                # print(file)
                i = i + 1
                copy_rename(file, str(i)+".eml", folder_address)

def copy_rename(old_file_name, new_file_name, destination_folder):
    print(destination_folder + '/' + new_file_name)
    print(old_file_name)
    shutil.copy(old_file_name,destination_folder + '/' + new_file_name)


if __name__ == "__main__":
	if len(sys.argv) is not 2:
		print 'Usage: python2.7 enron_mail_reader.py ' +' < Data directory name>'
		sys.exit(1)
	walk_dir(sys.argv[1])

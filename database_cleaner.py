import sys
import re
import os
import random
import time


def walk_dir(folder_address):
	cnt = 0
	i = 0.0
	files = [os.path.join(folder_address,f) for f in os.listdir(folder_address)]
	total_files = len(files)
	for file in files:
		i += 1
		with open(file) as f:
			if(filter(f)):
				os.remove(file)# delete empty file
				print("!!!Remove " + str(file))
				cnt += 1
			else:
				continue
			sys.stdout.write(str(i/total_files) + "% \r")
			sys.stdout.flush()
	print("This operation deletes : " + str(cnt) + " empty sfiles!!!!")
	

def filter(file):
	cnt_line = 0 
	for i,line in enumerate(file):
		cnt_line += 1
	if cnt_line < 1:
		return True
	else:
		return False
	# print(content)


if __name__ == "__main__":
	if len(sys.argv) is not 2:
		print 'Usage: python2.7 main.py ' +' < Data directory name>'
		sys.exit(1)
	walk_dir(sys.argv[1])

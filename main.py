"""
#	=========================================
#	This is the entrance file
#	=========================================
#	author: Y.W. Chen
#	Date:	Oct. 28, 2017
#	Version	1.0	Oct. 28, 2017	Tensorflow kernal
#	=========================================
"""
import sys
from autoencoder import Autoencoder
from parser import Parser
import csv
import numpy as np

if __name__ == "__main__":
	if len(sys.argv) is not 3:
		print 'Usage: python2.7 main.py ' + ' <keyword extraction directory name> ' + 'mode 0 ---> get keyword / mode 1 ---> data to autoencoder'
		sys.exit(1)
if(sys.argv[2] == '0'):
	ps = Parser()
	ps.extractdata(str(sys.argv[1]))
	data, reverse_data = ps.getDict()
	input_dim = len(data)
	print(data)
	print(input_dim)
	ps.save_csv()

elif(sys.argv[2] == '1'):
	hidden_dim = 2
	x = []
	y = []
	count = 0
	with open(str(sys.argv[1]), "r") as f:
		reader = csv.reader(f)
		for row in reader:
			input_dim = len(row)
			ae = Autoencoder(input_dim, hidden_dim)
			ae.train(np.array(row).reshape(1,input_dim))
			#print(input_dim)

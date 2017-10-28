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


if __name__ == "__main__":
	if len(sys.argv) is not 2:
		print 'Usage: python2.7 main.py ' + ' <keyword directory name> '
		sys.exit(1)


ps = Parser()
ps.extractdata(str(sys.argv[1]))

data, reverse_data = ps.getDict()
input_dim = len(data)
# print(data)
# print(input_dim)




ps.save_csv()

hidden_dim = 1
ae = Autoencoder(input_dim, hidden_dim)

# ae.train(data)

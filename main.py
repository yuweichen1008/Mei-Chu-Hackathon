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
	if len(sys.argv) is not 3:
		print 'Usage: python2.7 main.py ' + ' <keyword directory name> ' + 'mode 0 ---> parse data/ mode 1 --->autoencoder'
		sys.exit(1)
if(sys.argv[2] == '0'):
	ps = Parser()
	ps.extractdata(str(sys.argv[1]))
	data, reverse_data = ps.getDict()
	input_dim = len(data)
	print(data)
	print(input_dim)
	ps.save_csv()

else if(sys.argv[2] == '1'):
	hidden_dim = 2
	x = []
	y = []
	count = 0
	with open(csv_file, "r") as f:
		reader = csv.reader(f)
		for row in reader:
			x.append(row[0])
			y.append(row[1])
		keywords = np.hstack((x,y))
	ae = Autoencoder(input_dim, hidden_dim)

ae.train(data)

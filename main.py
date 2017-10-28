import sys
from autoencoder import Autoencoder
from parser import Parser


if __name__ == "__main__":
	if len(sys.argv) is not 2:
		print 'Usage: python2.7 main.py ' + ' <directory name> '
		sys.exit(1)


ps = Parser()
ps.extractdata(str(sys.argv[1]))

data, reverse_data = ps.getDict()
input_dim = len(data)
print(data)
# print(input_dim)

ps.save_csv()

'''
hidden_dim = 1
ae = Autoencoder(input_dim, hidden_dim)
'''
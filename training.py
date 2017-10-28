import collections
import csv
import sys
import re
import os
import numpy as np
import random
from difflib import SequenceMatcher


class Training:
	def __init__(self):
		self.classname = ['Hams', 'Spam']	# 0, 1
		self.feature = []
		self.keywords = []

	def load_csv(self, csv_file):
		x = []
		y = []
		count = 0
		with open(csv_file, "r") as f:
			reader = csv.reader(f)
			for row in reader:
				x.append(row[0])
				y.append(row[1])
			self.keywords = np.vstack((x,y))
			# print(keywords.shape)

	def train(self, train_folder):
		self.email_reader(train_folder)
		self.save_csv()

	def email_reader(self, address):
		emails = [os.path.join(address,f) for f in os.listdir(address)]
		for mail in emails:
			with open(mail) as m:
				self.feature.append(self.read_email_context(m))	# add the row to feature


	def read_email_context(self, mail):
		content = ""
		feature_vector = []
		for i,line in enumerate(mail):
			cnt_line = 0 
			if cnt_line <= i and i > 3: # prevent error
				cnt_line += 1
				if len(line) < 6:
					continue # prevent strange text
				if len(line) > 250:
					continue # prevent strange text
				if re.match(r'\s', line):
					continue # prevent strange text
				if re.match(r'\w', line):
					content += " " + line
		# print(content)
		for keyword in self.keywords:
			mail = SequenceMatcher(None, content, keyword) # content plain-text
			feature_vector.append(mail.ratio())
			print(max(feature_vector))

		return feature_vector # return feature list

	def save_csv(self):
		csv_columns = ['Keyword','Catagory']
		try:
			with open("data.csv", 'w') as csvfile:
				writer = csv.writer(csvfile)
				for row in self.feature:
					writer.writerow(row)
		except IOError as (errno, strerror):
			print("I/O error({0}): {1}".format(errno, strerror))
		return


if __name__ == "__main__":
	if len(sys.argv) is not 3:
		print 'Usage: python2.7 main.py ' + ' <keyword dircectory name> ' + ' <training data directory name>'
		sys.exit(1)


	ts = Training();
	keyword_csv_file = sys.argv[1]
	train_folder = sys.argv[2]
	
	# load keyword feature vector 1 * 3000
	ts.load_csv(keyword_csv_file)
	# load email and training the data.csv
	ts.train(train_folder)

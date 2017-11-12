"""
mail text data parsing

malicious: virus total, url analyser
phishing: phishing tank
spam mail
fraud mail 
trust
#	=========================================
#	author: Y.W. Chen
#	Date:	Oct. 26, 2017
#	Version	1.0	Oct. 26, 2017
#	Version 3.0 Oct. 28, 2017	Fail in shuffle function, no need to build the dict
#	Version 5.0 Oct. 29, 2017	Recover from version 1.0
#	=========================================

"""

import re
import os
import csv
import collections

class Parser(object):
	def __init__(self):
		self.dictionary = dict()
		self.reverse_dictionary = dict()
		self.all_words = []

	def extractdata(self, address = 'mails'):
		cnt_category = 0
		for catagory_dir in os.listdir(address):
			self.all_words[:] = []	# empty the all_words list
			if(str(catagory_dir)[0] != '.'):
				print("=====Category======")
				category_name = catagory_dir
				train_dir = address + '/' + category_name
				self.read_mails(train_dir)
				self.build_dataset(cnt_category)
				print(category_name + " : "+str(cnt_category))
				cnt_category += 1
				self.all_words[:] = []
				print("------------------")
				# print(os.listdir(category_name))
		self.concise()
		print("===================")
		print("vocabuary data size is " + str(len(self.dictionary)))

	def read_mails(self, train_dir):
		emails = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]
		for email in emails:
			# print(email) 
			# ex. mails/Spams/virus.txt
			with open(email) as m:
				for i,line in enumerate(m):
					if i != 0: #Bodt of email is only 1 line of text file
						if len(line) < 6:
							continue # prevent strange text
						if len(line) > 250:
							continue # prevent strange text
						if re.match(r'\s', line):
							continue # prevent strange text
						words = line
						pattern3 = re.compile("[^\w\d]+")
						words = pattern3.sub(' ',words)
						dicts = words.split()
						for word in dicts:
							if(len(word) < 10):
								self.all_words.append(word.lower())
		# print(dictionary)
		# self.concise()

	def build_dataset(self, catagory_number):
		count = collections.Counter(self.all_words).most_common(320)
		for word, _ in count:
			self.dictionary[word] = catagory_number;

	def save_csv(self):
		# not done here
		csv_columns = ['Keyword','Catagory']
		try:
			with open("keywords.csv", 'w') as csvfile:
				writer = csv.writer(csvfile)
				for key, value in self.dictionary.items():
					temp = [key, value]
					writer.writerow(temp)
				
		except IOError as (errno, strerror):
			print("I/O error({0}): {1}".format(errno, strerror))
		return


	def getDict(self):
		return self.dictionary, self.reverse_dictionary


	def concise(self):
		list_to_remove = self.dictionary.keys()
		for item in list_to_remove:
			if item.isalpha() == False: 
				del self.dictionary[item]
			elif len(item) == 1:
				del self.dictionary[item]

		count = collections.Counter(self.dictionary).most_common(200)
		self.reverse_dictionary = dict(zip(self.dictionary.values(), self.dictionary.keys()))
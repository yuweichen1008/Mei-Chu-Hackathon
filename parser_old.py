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
#	=========================================

"""
import re
import os
import csv
import sys
import collections
import numpy as np
from sklearn.utils import shuffle

class Parser(object):
	def __init__(self):
		self.dictionary = dict()
		self.reverse_dictionary = dict()
		self.emaillist = []
		self.catagorylist = []
	def extractdata(self, address = 'mails'):
		cnt_category = 0
		for catagory_dir in os.listdir(address):
			self.all_words[:] = []	# empty the all_words list
			if(str(catagory_dir)[0] != '.'):
				print("=====Category======")
				category_name = catagory_dir
				train_dir = address + '/' + category_name
				self.read_mails(train_dir, cnt_category)
				# self.build_dataset(cnt_category)
				cnt_category += 1
				print("------------------")
				# print(os.listdir(category_name))
		
		self.emaillist = np.array(self.emaillist).reshape(len(self.emaillist),1)
		self.catagorylist = np.array(self.catagorylist).reshape(len(self.catagorylist),1)
		# print(self.emaillist.shape)
		# print(self.catagorylist.shape)
		filelist = np.hstack((self.emaillist,self.catagorylist))
		# print(filelist)
		filelist = shuffle(filelist, random_state=273)
		
		self.process_words()

		self.concise()

		print("===================")
		print("vocabuary data size is " + str(len(self.dictionary)))

	def read_mails(self, train_dir, cnt_category):
		emails = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]
		for email in emails:
			self.emaillist.append(email)
			self.catagorylist.append(cnt_category)
		#print(len(self.emaillist))
		#print(len(self.catagorylist))

	def process_words(self):
		with open(email) as m:
			for i,line in enumerate(m):
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
					all_words.append(word.lower())
				self.build_dataset(cnt_category, all_words)
		# print(dictionary)
		# self.concise()

	def build_dataset(self, catagory_number, all_words):
		count = collections.Counter(all_words).most_common(60)
		for word, _ in count:
			self.dictionary[word] = catagory_number;

	def save_csv(self):
		# not done here
		csv_columns = ['Keyword','Catagory']
		try:
			with open("mydata.csv", 'w') as csvfile:
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
		print(count)
		self.reverse_dictionary = dict(zip(self.dictionary.values(), self.dictionary.keys()))
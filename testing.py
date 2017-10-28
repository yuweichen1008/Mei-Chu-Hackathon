import collections
import csv
import sys
import re
import os
import numpy as np
import random
from difflib import SequenceMatcher


class Testing:
    def __init__(self):
        self.classname = ['Hams', 'Spam', 'Advertising']   # 0, 1, 2
        self.catagory = []
        self.context = []

    def data_loader(self,testing_folder):
        for catagory_dir in os.listdir(testing_folder):
            if(catagory_dir[-4:] == '.csv'):
                print("it's csv")
                self.load_csv(os.path.join(testing_folder,catagory_dir))
                continue;
            # print(catagory_dir)
            if(catagory_dir == 'Ham'):
                self.email_reader(os.path.join(testing_folder,catagory_dir),0)
            elif(catagory_dir == 'Spam'):
                self.email_reader(os.path.join(testing_folder,catagory_dir),1)

    def load_csv(self, csv_file):
        count = 0
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                self.context.append(row[3])
                self.catagory.append(2) # advertisement

    def email_reader(self, address, catagory):
        emails = [os.path.join(address,f) for f in os.listdir(address)]
        for mail in emails:
            with open(mail) as m:
                self.context.append(self.read_email_context(m)) # add the row to feature
                self.catagory.append(catagory) # catagory
        # print(len(self.feature))
        # print(max(self.feature[0]))

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
        # print(len(feature_vector))
        return content # return feature list

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
    if len(sys.argv) is not 2:
        print 'Usage: python2.7 testing.py ' + ' <testing data directory name>'
        sys.exit(1)


    ts = Testing();
    testing_folder = sys.argv[1]
    ts.data_loader(testing_folder)
    print(len(ts.catagory))
    print(len(ts.context))
    # load keyword feature vector 1 * 3000
    # load email and training the data.csv
    # ts.train(train_folder)

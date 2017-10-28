#!/usr/bin/env python3
# requiremt: munpack (apt), googletrans (pip3)

import sys
import os
import re
import subprocess
import bs4
import googletrans


def gen_parsed_file(filename):
    # extract html file and plain content
    try:
        cmd = "munpack -t -f " + filename
        ret = subprocess.check_output(cmd.split())
    except subprocess.CalledProcessError:
        print(cmd + "is failed")
        sys.exit()
    
    
def read_file(filename):
    lines = ""
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                lines += line
    except FileNotFoundError:
        print(filename, "is not exit")

    return lines
        

def get_eml_content(filename):
    gen_parsed_file(filename)

    f_part1 = bs4.BeautifulSoup(read_file("part1"), "lxml").text
    f_part2 = bs4.BeautifulSoup(read_file("part2"), "lxml").text

    return [f_part1, f_part2]


def get_url(eml_content):
    # TODO: regular expression cannot cover all urls
    regex1 = "http[s]?://[a-zA-Z0-9\./_]+"
    regex2 = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

    urls = re.findall(regex1, eml_content[0])
    urls += re.findall(regex2, eml_content[0])
    urls += re.findall(regex1, eml_content[1])
    urls += re.findall(regex2, eml_content[1])


def translate_content(eml_content):
    # TODO: if part of words are english, googletrans cannot work correctly
    translator = googletrans.Translator()
    content0 = translator.translate(eml_content[0]).text
    content1 = translator.translate(eml_content[1]).text


def clear_generated_files():
    try:
        cmd = "rm part1 part2"
        ret = subprocess.run(cmd.split())
    except subprocess.CalledProcessError:
        print(cmd + "is failed")
        sys.exit()
    

def main():
    if (len(sys.argv) != 2) or (sys.argv[1][-4:] != ".eml"):
        print("Usage: ./parse_mail.py <filename>")

    # retrieve email content
    eml_content = get_eml_content(sys.argv[1]) 

    # retrieve url
    get_url(eml_content)

    # TODO: send url to phishing detect web site

    #  translate to English
    translate_content(eml_content)

    # TODO: send part1 and part2 to testing model

    clear_generated_files()


if __name__ == "__main__":
    main()

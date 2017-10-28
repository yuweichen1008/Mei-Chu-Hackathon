#!/usr/bin/env python3
# requiremt: munpack (apt), googletrans (pip3), urlextract (pip3)

import sys
import os
import re
import subprocess
import requests
import bs4
import googletrans
import urlextract


def gen_parsed_file(filename):
    # extract html file and plain content
    try:
        cmd = "munpack " + filename + " -t"
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
        

def decode_b64(content):
    try:
        cmd = "echo " + content + " | base64 --decode"
        ret = subprocess.check_output(cmd.split())
    except subprocess.CalledProcessError:
        print(cmd + "is failed")
        sys.exit()

    return ret


def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)


def get_eml_content(filename):
    gen_parsed_file(filename)

    # decode base64
    content1 = decode_b64(read_file("part1"))
    content2 = decode_b64(read_file("part2"))

    f_part1 = bs4.BeautifulSoup(read_file("part1"), "lxml").text
    f_part2 = bs4.BeautifulSoup(read_file("part2"), "lxml").text


    return [f_part1, f_part2]


def get_url(eml_content):
    extractor = urlextract.URLExtract()

    url_part1 = extractor.find_urls(eml_content[0])
    url_part2 = extractor.find_urls(eml_content[1])

    print(url_part1 + url_part2)
    return url_part1 + url_part2


def determine_url_type(vt_res):
    # return the type that more detection sites identify it is as
    rec = []
    parse_vt_res = vt_res.split()

    for i in range (len(parse_ret)):
        if parse_ret[i] == "True,":
            rec.append(parse_ret[i + 2][1:])

    add_up = {}

    # count which type occurs most of time
    for t in rec:
        if t in add_up:
            add_up[t] += 1
        else:
            add_up[t] = 1

    return sorted(add_up.keys())[0]
            

def get_virus_total_ret(url):
    # virus total scan url
    url_scan = "https://www.virustotal.com/vtapi/v2/url/scan"
    # virus total report url
    url_report = "https://www.virustotal.com/vtapi/v2/url/report"
    # my virus total api key
    apikey = "6a71c63f069c4b966a6c8019b983a89f2132df9e7e212ad3fd9c101d80f74f05"

    # malicious url scan
    params = {'apikey': apikey, 'url': url}
    response = requests.post(url_scan, data=params)

    # get malicious url report from virus total
    params = {'apikey': apikey, 'resource': url}
    response = requests.get(url_report, params=params)

    if "True" in response.json():
        return [determine_url_type(response.json())]
    else:
        return ["clean"]
    

def detect_url_type(url_list):
    ret_type = []

    for url in url_list:
        ret_type += get_virus_total_ret(url)

    return ret_type
            

def det_type_mail(stat_type):
    if len(stat_type) == 0:
        return "clean"

    add_up = {}
    for t in stat_type:
        if t in add_up:
            add_up[t] += 1
        else:
            add_up[t] = 1

    return sorted(add_up.keys())[0]
            


def translate_content(eml_content):
    translator = googletrans.Translator()
    content0 = translator.translate(eml_content[0]).text
    content1 = translator.translate(eml_content[1]).text

    return [content0, content1]


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

    # translate to English
    trans_content = translate_content(eml_content)

    # retrieve url
    url_list = get_url(trans_content)

    # send url to url malicious detection site help us detect url type 
    ret_type = detect_url_type(url_list)

    # determine the type of mail
    type_mail = det_type_mail(ret_type)

    # send plain content to testing model
    dst_path = "./text_file/"
    for context in trans_content:
        write_file(dst_path + sys.argv[1][:-4] + ".txt", context)

    clear_generated_files()


if __name__ == "__main__":
    main()

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
        

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)


def get_eml_content(filename):
    gen_parsed_file(filename)

    f_part1 = bs4.BeautifulSoup(read_file("part1"), "lxml").text
    f_part2 = bs4.BeautifulSoup(read_file("part2"), "lxml").text

    return [f_part1, f_part2]


def get_url(eml_content):
    extractor = urlextract.URLExtract()

    url_part1 = extractor.find_urls(eml_content[0])
    url_part2 = extractor.find_urls(eml_content[1])

    print(url_part1 + url_part2)
    return url_part1 + url_part2


def get_ret_type(html_content):
    pretar_str = '<div class="labeltitlesmallresult">'
    tar_addr = html_content.find(pretar_str) + len(pretar_str)
    ret_type = html_content[tar_addr, tar_addr + 16].split("</div>")[0]
    return [ret_type]


def detect_url_type(url_list):
    base_url = "https://global.sitesafety.trendmicro.com"
    target_url = "https://global.sitesafety.trendmicro.com/result.php"

    ret_type = []

    for url in url_list:
        payload = {"urlname": url}
        with requests.session() as session:
            session.get(base_url)
            res = session.post(target_url, data=payload)

        ret_type += get_ret_type(res.text)

    return ret_type
            
        
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

    # retrieve url
    url_list = get_url(eml_content)

    # send url to trend site safety center to help us detect url type 
    ret_type = detect_url_type(url_list)

    # translate to English
    trans_content = translate_content(eml_content)

    # TODO: send part1 and part2 to testing model
    dst_path = "./text_file/"
    for context in trans_content:
        write_file(dst_path + sys.argv[1][:-4] + ".txt", context)

    clear_generated_files()


if __name__ == "__main__":
    main()

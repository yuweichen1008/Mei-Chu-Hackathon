#!/usr/local/bin/python3

import eml_parser
import json
import datetime
import sys

def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial


with open(sys.argv[1], 'rb') as fhdl:
    raw_email = fhdl.read()

parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email)

print(parsed_eml["header"]["subject"])
print(parsed_eml["header"]["from"])
print(parsed_eml["header"]["to"][0])
#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from pprint import pprint

with open('train.json') as data_file:    
    data = json.load(data_file)


for c in data:
	print c['cuisine']
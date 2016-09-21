#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
from pprint import pprint

def imprimir(d,c):
	ans = ""
	for k in d.keys():
		ans += str(d[k]) + ","
	return ans +c


with open('train.json') as data_file:    
    data = json.load(data_file)

# pprint(data)

ingredients = []
dict_ingredients = {}

for c in data:
	for i in c['ingredients']:
		dict_ingredients[i] = 0

for c in data:
	if 
#!/usr/bin/env python


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
from pprint import pprint

with open('train.json') as data_file:    
    data = json.load(data_file)


dict_ingredients = {}

for c in data:
	# if c['cuisine'] == 'brazilian':
		if c['cuisine'] not in dict_ingredients:
			dict_ingredients[c['cuisine']] = []

		for i in c['ingredients']:
			dict_ingredients[c['cuisine']].append(i)


printed = []
ingredients = {}
for c in dict_ingredients.keys():
	for i in dict_ingredients[c]:
		if (c,i) not in printed:
			qtd = dict_ingredients[c].count(i)
			if qtd >= 100:
				print c + "," + i + "," + str(qtd)
				printed.append((c,i))
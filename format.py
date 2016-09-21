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

# with open('ingred_freq_by_cuisine_100.csv') as data_file:    
ingred100 = open('ingred_freq_by_cuisine_100.csv','r')

# pprint(data)

ingredients = []
dict_ingredients = {}

# for c in data:
# 	for i in c['ingredients']:
# 		if i not in ingredients:
# 			dict_ingredients[i] = 0
# 			ingredients.append(i)
for line in ingred100:
	temp = line.split(",")
	if temp[1] not in ingredients:
		dict_ingredients[temp[1]] = 0
		ingredients.append(temp[1])

ans = ""
for i in ingredients:
	ans += i + ","
print ans + "target"
# print len(ingredients), len(dict_ingredients.keys())

for c in data:
	temp = dict_ingredients.copy()
	for i in c['ingredients']:
		if i in ingredients:
			temp[i] = 1
	print imprimir(temp,c['cuisine'])
	# print c['cuisine'], c['ingredients'],len(c['ingredients']), len(temp.keys()), len(ingredients)
	# print "##############################################"



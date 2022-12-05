from functools import reduce
import csv
import re

file = open("dataset.csv","r")
keys = file.readline()
reader = csv.reader(file, delimiter=",", quotechar = '"')
data = [row for row in reader]
file.close()

keys = list(keys.split(","))
keys = list(map(lambda x: x.replace('"', ""), keys))
regexp = '\W+'
keys[len(keys) - 1] = re.sub(regexp,'', keys[len(keys) - 1])
print(keys)

def to_int(x):
	try:
		x = int(x)
	except ValueError:
		pass
	return x

def clean_one(x):
	x = x.replace('"', '')
	x = to_int(x)
	return x

def clean_row(l):
	l = l[0].split(",")
	l = list(map(clean_one, l))
	return l

def to_dict(keys, values):
	if not len(keys) == len(values):
		raise AttributeError()
	dictionary = {}
	for i in range(len(keys)):
		dictionary[keys[i]] = values[i]
	return dictionary

data = list(map(clean_row, data))
data = list(map(lambda x: to_dict(keys, x), data))
print(data)
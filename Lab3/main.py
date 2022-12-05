from functools import reduce
import csv
import re

with open("dataset.csv","r") as file:
	keys = file.readline()
	reader = csv.reader(file, delimiter=",", quotechar = '"')
	data = [row for row in reader]

keys = list(keys.split(","))
keys = list(map(lambda x: x.replace('"', ""), keys))
regexp = '\W+'
keys[len(keys) - 1] = re.sub(regexp,'', keys[len(keys) - 1])

def to_number(x):
	try:
		x = int(x)
	except ValueError:
		try:
			x = float(x)
		except ValueError:
			pass
	return x

def clean_one(x):
	x = x.replace('"', '')
	x = to_number(x)
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

prices = list(map(lambda x: round(x['price'], 2), data))
prices_sum = round(reduce(lambda x, y: x + y, prices), 2)
avg_price = round(prices_sum / len(prices), 2)

print(f"Сумма всех цен: {prices_sum}\nКол-во позиций: {len(prices)}\nСредняя цена: {avg_price}")
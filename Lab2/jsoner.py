import json
import os.path
from pprint import pprint

class Jsoner:

	_file_name = "saves.json"
	_enc = 'utf-8'
	_ind = 4

	@staticmethod
	def save(obj, obj_name):
		if not os.path.isfile(Jsoner._file_name):
			Jsoner.clean()
		data = json.load(open(Jsoner._file_name, mode='r', encoding=Jsoner._enc))
		data[obj_name] = obj
		json.dump(data, open(Jsoner._file_name, mode='w', encoding=Jsoner._enc), indent = Jsoner._ind)

	@staticmethod
	def clean():
		json.dump({}, open(Jsoner._file_name, "w", encoding = Jsoner._enc), indent = Jsoner._ind)

	@staticmethod
	def delete_obj(obj_name):
		data = json.load(open(Jsoner._file_name, "r", encoding = Jsoner._enc))
		if obj_name in data:
			del data[obj_name]
			json.dump(data, open(Jsoner._file_name, "w", encoding = Jsoner._enc), indent =Jsoner._ind)
			return True
		return False

	@staticmethod
	def load(obj_name):
		data = json.load(open(Jsoner._file_name, "r", encoding = Jsoner._enc))
		if not obj_name in data:
			raise AttributeError(f"there is no object with this name `{obj_name}`")
		return data[obj_name]

	@staticmethod
	def show_all():
		data = json.load(open(Jsoner._file_name, "r", encoding = Jsoner._enc))
		pprint(data, depth = 4, sort_dicts = False, indent = Jsoner._ind, compact = False)

	@staticmethod
	def show_obj(obj_name):
		data = Jsoner.load(obj_name)
		print(f"Saved '{obj_name}':")
		pprint(data, depth = 4, sort_dicts = False, indent = Jsoner._ind, compact = False)
from urllib import request,parse
import json
import requests

#synchronous
def http_get(url):
	"""
	Performs a synchronous GET request on the given url.

	:param url: url of the API
	:type url: string

	"""
	try:
		resp = request.urlopen(url)
	except Exception:
		print("Invalid url. Connection Failed.")
		exit(1)
	data = resp.read()
	data = json.loads(data.decode("UTF-8"))
	return data

#synchronous
def http_post(url,post_data):
	"""
	Performs a synchronous POST request on the given url.

	:param url: url of the API
	:type url: string
	:param post_data: Key-value pairs of the request payload.
	:type post_data: dict 

	"""
	data = requests.post(url,post_data)
	data = data.json()
	return data


class table:

	def __init__(self,PATH):
		try:
			file = open(PATH,'r')
		except:
			print("No file detected.")
			exit(1)
		lines = file.readlines()
		data = []
		for line in lines:
			fragment = line.split(',')
			x = fragment[len(fragment)-1]
			x = x[:-1]
			fragment[len(fragment)-1] = x
			data.append(fragment)
		self.data = data

	def get_row_count(self):
		return (len(self.data))

	def get_column_count(self):
		return (len(self.data[0]))

	def get_column(self,name):
		count = 0
		try:
			for i in self.data[0]:
				if i == name:
					break
				count = count + 1
			column = []
			for item in self.data:
				column.append(item[count])
			return column
		except:
			print("ERROR: column does not exist")

	def get_row(self,inde):
		for fragment in self.data:
			if fragment[0] == inde:
				return fragment
	def get_array(self):
		return self.data


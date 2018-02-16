import os

def scan(dir):
	os.chdir(dir)
	return os.listdir()

def recscandir(path):
	os.chdir(path)
	data = os.listdir()
	dir = searchdir(path, data)
	datanorm = []
	for e in data:
		datanorm.append(path+'/'+e)
	result = datanorm
	for d in dir:
		da = recscandir(d)
		for e in da:
			result.append(e)
	return result
	
def getextension(path):
	if os.pathis.isfile(path):
		return path.split('.')[-1]
	return None

def searchdir(path, list):
	dir = []
	for e in list:
		p = path + '/' + e
		if os.path.isdir(p):
			dir.append(p)
	return dir
	
def searchfile(path, list):
	file = []
	for e in list:
		f = path + '/' + e
		if os.path.isfile(f):
			file.append(f)
	return file
	
def searchdirlist(list):
	dir = []
	for p in list:
		if os.path.isdir(p):
			dir.append(p)
	return dir	

def searchfilelist(list):
	file = []
	for f in list:
		if os.path.isfile(f):
			file.append(f)
	return file

def normalizepath(path):
	path = path.replace("\\", "/")
	#path = path.replace(" ", "\ ")
	return path

def readfile(path):
	try:
		with open(path,'r') as file:
			data = file.read()
		return data
	except:
		return None
		
def writefile(path, data):
	try:
		with open(path, "w+") as file:
			file.write(data)
		return True
	except:
		return False

def minimizecode(code):
	code = code.replace("\n", " ")
	code = code.replace("\t", " ")
	return code
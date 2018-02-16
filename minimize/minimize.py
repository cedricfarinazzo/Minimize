import sys, os, time
import fun_minimize

def main():

	space = " " * 9
	print("\n"+space+"   = = = = = = = = = = = = = = = ");
	print(space+" |                               |")
	print(space+" |           MINIMIZE            |")
	print(space+" |             1.0.1             |")
	print(space+" |                               |")
	print(space+" |                               |")
	print(space+"   = = = = = = = = = = = = = = = \n");
	
	start = time.time()



	try:
		path = fun_minimize.normalizepath(input("path : "))
		folder = os.path.dirname(path)
		Npath = folder + "-min/"
		print(Npath)
		try:
			os.mkdir(Npath)
		except:
			pass
		
		scan = fun_minimize.recscandir(path)
		dir = fun_minimize.searchdirlist(scan)
		file = fun_minimize.searchfilelist(scan)
		
		for d in dir:
			p = Npath + d.split(path)[-1]
			try:
				os.mkdir(p)
			except:
				continue
				
		save = 0
		for f in file:
			code = fun_minimize.readfile(f)
			if code != None:
				minicode = fun_minimize.minimizecode(code)
				save += len(code) - len(minicode)
				fun_minimize.writefile(Npath + f.split(path)[-1], minicode)
		print("\n[+] Save {} bits ! ".format(save))
		
		
	except:
		print("\n[!] Path not found ! ")
	
	
	print("\n[+] Minimize in {} s\n".format(time.time() - start))
	
	print("\n[+] Appuyer sur une touche pour quitter ...")
	sys.exit(0)
	
if __name__ == "__main__":
	main()

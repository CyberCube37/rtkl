with open(esej.txt) as esej:
	for vrstica in esej:
		a = vrstica.split()
		for i in a:
			if len(i) < 3:
				manj_kot3 += 1
			if len(i) > 8:
				vec_kot8 += 1
		if manj_kot3 == 0 and vec_kot8 ==0:
			print('lep esej')
		else:
			print('manj kot 3:', manj_kot3)
			print('vec kot 8:', vec_kot8)

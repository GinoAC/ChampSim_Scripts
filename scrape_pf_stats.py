import os

<<<<<<< HEAD
out = open("pfoutuseful.txt","w+")

for fil in os.listdir("."):
=======
out = open("pfout","w+")

for fil in os.listdir("."):
	#print fil
>>>>>>> 7af0ba3ed29758c0ac17afdd0e8c46136a69fbaa
	if fil[-4:] != '.txt':
		continue
	f = open(fil, "r")
	l = ""
	for line in f:
		s = line.strip()
		s = s.split(" ")
		c = []
		for a in s:
<<<<<<< HEAD
			if a != '':
				c.extend([a])
		if len(c) < 3:
			continue
		if c[0] == "L2" and c[1] == "PREFETCHES":
			#if c[3] == '0':
			#	l += '0' + " "
			#else:
			l += c[3] + " "
		elif c[0] == "L2" and c[1] == "USEFUL":
			l += c[3] + " " #+ c[7] + " "
=======
			#print a
			if a != '':
				c.extend([a])
		#print s
		#print c
		#print len(c)
		if len(c) < 3:
			continue
		if c[0] == "L2" and c[1] == "PREFETCHES":
			if c[3] == '0':
				l += '0' + " "
			else:
				l += c[3] + " "
		elif c[0] == "L2" and c[1] == "USEFUL":
			l += c[3] + " " + c[7] + " "
	#print l	
>>>>>>> 7af0ba3ed29758c0ac17afdd0e8c46136a69fbaa
	out.write(fil + " ")		
	out.write(l)
	out.write("\n")	

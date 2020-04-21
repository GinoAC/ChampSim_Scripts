import os

out = open("pfoutuseful.txt","w+")

for fil in os.listdir("."):
	if fil[-4:] != '.txt':
		continue
	f = open(fil, "r")
	l = ""
	for line in f:
		s = line.strip()
		s = s.split(" ")
		c = []
		for a in s:
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
	out.write(fil + " ")		
	out.write(l)
	out.write("\n")	

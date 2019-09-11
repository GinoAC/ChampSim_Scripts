import os

out = open("pfout","w+")

for fil in os.listdir("."):
	#print fil
	if fil[-4:] != '.txt':
		continue
	f = open(fil, "r")
	l = ""
	for line in f:
		s = line.strip()
		s = s.split(" ")
		c = []
		for a in s:
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
	out.write(fil + " ")		
	out.write(l)
	out.write("\n")	

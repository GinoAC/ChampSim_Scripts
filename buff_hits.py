import os

out = open("timeliness_hits.txt","w+")

fil_cut = ""
for fil in os.listdir("."):
	if fil[-4:] != '.txt':
		continue
	f = open(fil, "r")
	l = ""
	
	fil_cut = fil.split("-")
	if(len(fil_cut) >= 2):
		fil_cut = fil_cut[0] + "-" + fil_cut[1]	
	else:
		continue

	for line in f:
		s = line.strip()
		s = s.split(" ")
		c = []
		for a in s:
			if a != '':
				c.extend([a])
		if len(c) < 3:
			continue
		if c[0] == "L2C" and c[1] == "LOAD" and c[2] == "ACCESS:":
			l += c[7] + " "

		if len(c) < 6:
			continue

		if c[0] == "miss" and c[2] == "pf":
			l += c[5] + " "
		if c[0] == "Cache" and c[6] == "pq:":
			l += c[7] + " "
		if c[0] == "Cache" and c[6] == "MSHR:":
			l += c[7] + " "

	out.write(fil_cut + " ")		
	out.write(l)
	out.write("\n")	

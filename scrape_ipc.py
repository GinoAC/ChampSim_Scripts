import os

out = open("ipc_stats.txt","w+")

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
		if c[0] == "CPU" and c[2] == "cumulative":
			l += c[4] + " " #+ c[7] + " "
	out.write(fil + " ")		
	out.write(l)
	out.write("\n")	

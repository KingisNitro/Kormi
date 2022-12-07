f = open("6-input.txt", "r")

for line in f:
	for i in range (0, len(line)-4):
		for j in line[i:i+14]:
			if line[i:i+14].count(j) > 1:
				break
		else:
			print(i+14, line[i:i+14])
			quit(1)
	
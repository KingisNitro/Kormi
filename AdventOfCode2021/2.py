f = open("2-input.txt", "r")

# second part of the puzzle
hor, ver, aim = 0, 0, 0
for line in f:
	words = line.split()
	if words[0] == "forward":
		hor += int(words[1])
		ver += int(words[1]) * aim
	elif words[0] == "down":
		aim += int(words[1])
	elif words[0] == "up":
		aim -= int(words[1])
print(hor*ver)

'''
# first part of the puzzle
hor, ver = 0, 0
for line in f:
	words = line.split()
	if words[0] == "forward":
		hor += int(words[1])
	elif words[0] == "down":
		ver += int(words[1])
	elif words[0] == "up":
		ver -= int(words[1])
print(hor*ver)
'''
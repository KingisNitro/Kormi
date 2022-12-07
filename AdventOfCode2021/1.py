f = open("1-input.txt", "r")

# second part of the puzzle
window = [0, 0]
increase = 0
line = []
for i in f:
	line.append(int(i[:-1]))
for i in range(0, len(line)-3):
	for j in range(0, 3):
		window[0] += line[i+j]
		window[1] += line[i+1+j]
	print(window[1], window[0])
	if window[1] > window[0]:
		increase += 1
	window = [0, 0]
print(increase)


''' 
# first part of the puzzle
prev_line = ""
for line in f:
	if prev_line == "":
		prev_line = line[:-1] 
		continue
	if int(line[:-1]) > int(prev_line):
		increase += 1
	prev_line = line[:-1] 
print(increase)
'''

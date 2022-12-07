def most_common(list_of_inputs, index):
	binary = 0
	for i in list_of_inputs:
		binary += int(i[index])
	return 1 if binary >= len(list_of_inputs)/2 else 0
	
def least_common(list_of_inputs, index):
	if len(list_of_inputs) == 1:
		return int(list_of_inputs[0][index])
	binary = 0
	for i in list_of_inputs:
		binary += int(i[index])
	return 1 if binary < len(list_of_inputs)/2 else 0

f = open("3-input.txt", "r")
input = []
for line in f:
	input.append(line[:-1])
	
input1 = input
input2 = input
for position in range(0, len(input1[0])):
	o = most_common(input1, position)
	c = most_common(input2, position)
	o2, co2 = [], []
	for i in input1:
		if int(i[position]) == o:
			o2.append(i)
	print(position, c, len(input2), input2)
	for i in input2:
		if len(input2) == 1:
			co2.append(i)
			break
		if int(i[position]) != c:
			co2.append(i)	
	input1 = o2
	input2 = co2
print(input1)

print(int(input1[0], 2)*int(input2[0], 2))

'''
#second part of the puzzle 
# o2
input1 = input
for position in range(0, len(input1[0])):
	b = most_common(input1, position)
	new_list = []
	for i in input1:
		if int(i[position]) == b:
			new_list.append(i)
	input1 = new_list
print(input1)

# co2
input2 = input
for position in range(0, len(input2[0])):
	b = least_common(input2, position)
	new_list = []
	for i in input2:
		if int(i[position]) == b:
			print(i, i[position], b)
			new_list.append(i)
			print(f"I appended {i}")
	input2 = new_list
print(input2)

print(int(input1[0], 2)*int(input2[0], 2))
'''

'''
# first part of the puzzle
first = 0
count = 0
for line in f:
	if first == 0:
		binary = [0] * (len(line) - 1)
		first = 1
	count += 1
	for i in range(0, (len(line) - 1)):
		binary[i] += int(line[i])

text = ""
text2 = ""
for i in binary:
	if i > count//2:
		text += "1"
		text2 += "0"
	else:
		text += "0"
		text2 += "1"
		
print(int(text, 2)*int(text2, 2))
'''

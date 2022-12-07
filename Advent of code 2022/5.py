f = open("5-input.txt", "r")

stacks_finished = 0
stacks = []
for line in f:
	if len(line) == 36:
		stacks.append(line[:-1])
	elif len(line) == 1:
		num_stacks = max(stacks[-1])
		stacks2 = [""] * int(num_stacks)
		for i in stacks[-2::-1]:
			for n, j in enumerate(i[1::4]):
				if j != " ":
					stacks2[n] += j
	else:
		numbers = line[:-1].split(" ")[1::2]
		""" Original task 1
		for i in range(0, int(numbers[0])):
			stacks2[int(numbers[2])-1] += stacks2[int(numbers[1])-1][-1]
			stacks2[int(numbers[1])-1] = stacks2[int(numbers[1])-1][:-1]
		"""
		stacks2[int(numbers[2])-1] += stacks2[int(numbers[1])-1][-int(numbers[0]):]
		stacks2[int(numbers[1])-1] = stacks2[int(numbers[1])-1][:-int(numbers[0])]
		
text = ""
for i in stacks2:
	text += i[-1]
print(text)
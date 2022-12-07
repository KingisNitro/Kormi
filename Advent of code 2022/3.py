f = open("3-input.txt", "r")

def get_priority(x):
	if ord(x) > 96:
		return ord(x)-96
	return ord(x)-38

objects = []
groups = []
count = 0
for line in f:
	half = int((len(line)-1)/2)
	objects.append((line[:half], line[half:-1]))
	if (count % 3) == 0:
		groups.append([])
	groups[-1].append(line[:-1])
	count += 1

total_priority = 0
for o in objects:
	for j in o[0]:
		if j in o[1]:
			total_priority += get_priority(j)
			break
print(total_priority)

total_priority = 0
for group in groups:
	for i in group[0]:
		if i in group[1] and i in group[2]:
			total_priority += get_priority(i)
			break
print(total_priority)
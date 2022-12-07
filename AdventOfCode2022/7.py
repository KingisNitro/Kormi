f = open("7-input.txt", "r")

dict = {}

current = ""

for line in f:
	words = line.split()
	if words[0] == "$":
		if words[1] == "cd":
			if words[2] == "..":
				current = "_".join([i for i in current.split("_")][:-1])
			else:
				current += "_" + words[2]
		else:					# ls
			if current in dict:
				print(current)
				print("Houston we have a problem!!")
				quit(1)
			dict[current] = []
	elif words[0] == "dir":
		dict[current].append(words[1])
	else:						# files
		dict[current].append(words[1])
		dict[current + "_" + words[1]] = int(words[0])

def check_size(name):
	size = 0
	if isinstance(dict[name], int):
		return dict[name]
	for i in dict[name]:
		if isinstance(dict[name + "_" + i], int):		# i is a file
			size += dict[name + "_" + i]
		if isinstance(dict[name + "_" + i], list):		# i is a directory
			size_dir = check_size(name + "_" + i)
			size += size_dir
	return size
	
smaller = []
dir_to_delete = 70000000
needed = check_size("_/") - 40000000

for key in dict:
	if isinstance(dict[key], int) == 0:
		size = check_size(key)
		if size <= 100000:
			smaller.append(size)
		if needed < size and size < dir_to_delete:
			dir_to_delete = size
			dir = key
	#print(key, size)
	
print(f"Total size taken up by directories is {needed + 40000000}")
print(f"Needed: {needed}")	
print(f"Total space taken up by small directories: {sum(smaller)}")
print(f"Smallest dir to delete is the size of {dir_to_delete} and it's {dir}")
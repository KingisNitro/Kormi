f = open("7-input.txt", "r")

dict = {}

current = ""

for line in f:
	words = line.split()
	if words[0] == "$":							# commands
		if words[1] == "cd":						# changing directory
			if words[2] == "..":						# going up
				current = "_".join([i for i in current.split("_")][:-1])
			else:										# going into a directory
				current += "_" + words[2]
		else:										# listing contents of directory
			if current in dict:							# checking for uniqueness of files/directories
				print(current)
				print("Houston we have a problem!!")
				quit(1)
			dict[current] = []
	elif words[0] == "dir":								# the listed item is a directory
		dict[current].append(words[1])
	else:												# the listed item is a file
		dict[current].append(words[1])
		dict[current + "_" + words[1]] = int(words[0])

def check_size(name):
	if isinstance(dict[name], int):		# check if it's a file
		return dict[name]				# if so, return its size
	size = 0
	for i in dict[name]:		# if it is a dictionary, check its contents
		size_dir = check_size(name + "_" + i)
		size += size_dir		# add the size of its contents to the directory size
	return size
	
smaller = []
dir_to_delete = 70000000
needed = check_size("_/") - 40000000

for key in dict:
	if isinstance(dict[key], int) == 0:		# if a directory,
		size = check_size(key)
		if size <= 100000:					# is it a small directory?
			smaller.append(size)
		if needed < size and size < dir_to_delete:	# is it a directory that would free up enough space upon deletion?
			dir_to_delete = size
			dir = key
	
print(f"Total size taken up by directories is {needed + 40000000}")
print(f"Needed: {needed}")	
print(f"Total space taken up by small directories: {sum(smaller)}")
print(f"Smallest dir to delete is the size of {dir_to_delete} and it's {dir}")
elves, calories, max_calories = [], 0, 0

f = open("1-input.txt", "r")

for line in f:
	if line == "\n":
		elves.append(calories)
		if calories > max_calories:
			max_calories = calories
		calories = 0
	else:
		calories += int(line)

elves.sort(reverse=True)

print(max_calories, elves[0]+elves[1]+elves[2])

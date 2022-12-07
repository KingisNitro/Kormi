f = open("4-input.txt", "r")
overlaps, overlaps2 = 0, 0
for line in f:
	words = line.split(",")
	w11, w12 = words[0].split("-")
	w21, w22 = words[1][:-1].split("-")
	w11, w12, w21, w22 = int(w11), int(w12), int(w21), int(w22)
	if (w11 <= w21 and w12 >= w22) or (w11 >= w21 and w12 <= w22):
		overlaps += 1 # check if they are contained wholly
	if (w21 <= w12 and w12 <= w22) or (w11 <= w22 and w22 <= w12):
		overlaps2 += 1 # check if parts are contained
print(overlaps, overlaps2)
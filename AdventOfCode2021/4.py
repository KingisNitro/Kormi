f = open("4-input.txt", "r")

boards = []
bingo = -1

for line in f:
	words = line.split()
	if len(line.split()) == 0:
		boards.append([])
		bingo += 1
	elif len(words) == 1:
		called = line.split(",")
		called[-1] = called[-1][:-1]
	elif len(line.split()) > 1:
		boards[bingo].append(line.split())

def check_bingo(board):
	vert = [0] * 5
	for i in board:
		if i.count("") == 5:
			return True
		for j in range(0, 5):
			if i[j] == "":
				vert[j] += 1
	if vert.count(5) >= 1:
		return True
	return False

def get_score(board):
	score = 0
	for j in range(0, 5):
		for k in range(0, 5):
			if boards[i][j][k] != "":
				score += int(boards[i][j][k])
	return score


count = 0
winning_boards = []			# unique boards
for c in called:
	for i in range(0, len(boards)):
		for j in range(0, 5):
			for k in range(0, 5):
				if  boards[i][j][k] == c:
					boards[i][j][k] = ""
		if check_bingo(boards[i]):
			if count == 0:						# first part of the puzzle
				score = get_score(boards[i])
				print(f"Board {i+1} just won! It is the first board to win.")
				print(boards[i])
				print(score*int(c))			
			if i not in winning_boards:			# second part of the puzzle starts here and is below
				winning_boards.append(i)
				count += 1
		if count == 100:
			score = get_score(boards[i])
			print(f"Board {i+1} just won! It is the last board to win.")
			print(boards[i])
			print(score*int(c))
			quit(1)
		
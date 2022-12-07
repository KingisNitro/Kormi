dictionary = {
			"A" : "rock", 
			"X" : "rock", 
			"B" : "paper", 
			"Y" : "paper",
			"C" : "scissors",
			"Z" : "scissors"
			}
moves = {
		"rock" 		: 0, 
		"paper" 	: 1, 
		"scissors" 	: 2
		}
res = {
		"X" : -1,
		"Y" : 0,
		"Z" : 1
		}
scoring = {i: 3*res[i]+3 for i in res}
	
results = {(a,b):a-b for a in (0, 1, 2) for b in (0, 1, 2)}			# my move, opponent: result
my_moves = {(i[1], results[i]):i[1]+results[i] for i in results}	# opponent, result: my move
my_moves[(2,1)] = 0
my_moves[(0,-1)] = 2

f = open("2-input.txt", "r")
score, score2 = 0, 0
for line in f:
	"""Original guide"""
	words = [word for word in line.split()]
	opponent, me = dictionary[words[0]], dictionary[words[1]] 
	result = results[(moves[me], moves[opponent])]
	if result == 2:
		result = -1
	elif result == -2:
		result = 1
	points = moves[me] + 1 + 3*result+3
	score += points
	
	"""New guide"""
	me = my_moves[(moves[opponent], res[words[1]])]
	points = me + 1 + scoring[words[1]]
	score2 += points

print(score, score2)


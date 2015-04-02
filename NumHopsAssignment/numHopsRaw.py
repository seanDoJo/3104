import math
def NumHops(x,l,memo):
	if(l < 0):
		return ("", float("inf"))
	if(x > 101):
		return ("", float("inf"))
	if(x == 101):
		return ("101", 0)
	if((x,l) in memo):
		return memo[(x,l)]
	minPath = float("inf")
	minStr = ""
	lives = l
	if(math.sqrt(x) % 1 == 0):
		lives = l-1
	elif(x == 42):
		lives = l+1
	for i in range(4):
		(stri, iterat) = NumHops(x+i+1, lives, memo)
		if(iterat + 1 < minPath):
			minStr = stri
			minPath = (1 + iterat)
	memo[(x,l)] = (str(x) + " " + minStr, minPath)
	return (str(x) + " " + minStr, minPath)

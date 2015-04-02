import math
def NumHops(x, l, memo):
	if(l < 0):
		return ("", float("inf"))
	if(x > 101):
		return ("", float("inf"))
	if(x == 101):
		return ("101", 0)
	if((x,l) in memo):
		return memo[(x,l)]
	if(math.sqrt(x) % 1 == 0):
		minPath = float("inf")
		minStr = ""
		for i in range(4):
			(stri,iterat) = NumHops(x+i+1, l-1, memo)
			if((iterat + 1) < minPath):
				minStr = stri
				minPath = (1 + iterat)
		memo[(x,l)] = (str(x) + " " + minStr,minPath)
		return (str(x) + " " + minStr,minPath)
	if(x == 42):
		minPath = float("inf")
		minStr = ""
		for i in range(4):
			(stri,iterat) = NumHops(x+i+1, l+1, memo)
			if((iterat + 1) < minPath):
				minStr = stri
				minPath = (1 + iterat)
		memo[(x,l)] = (str(x) + " " + minStr,minPath)
		return (str(x) + " " + minStr,minPath)
	minPath = float("inf")
	minStr = ""
	for i in range(4):
		(stri,iterat) = NumHops(x+i+1, l, memo)
		if((iterat + 1) < minPath):
			minStr = stri
			minPath = (1 + iterat)
	memo[(x,l)] = (str(x) + " " + minStr,minPath)
	return (str(x) + " " + minStr,minPath)

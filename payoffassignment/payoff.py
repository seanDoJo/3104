def payoff(B, R, j, inv, memo):
	if(B < 0):
		return(("", float("-inf")))
	if(R < 0):
		return(("", float("-inf")))
	if(j == 0):
		return(("", 0))
		
	Pj = inv[1][j-1]
	Cj = inv[0][j-1]
	Rj = inv[2][j-1]

	if((B,R,j) in memo):
		(seq, profit) = memo[(B,R,j)]
		return seq, profit

	(stri, none) = payoff(B, R, j-1, inv, memo)
	(strj, some) = payoff(B-Cj, R-Rj, j-1, inv, memo)
	
	if(none < Pj + some):
		memo[(B,R,j)] = (str(j) + " " + strj, Pj + some)
		return (str(j) + " " + strj, Pj + some)
	else:
		memo[(B,R,j)] = (stri, none)
		return (stri, none)

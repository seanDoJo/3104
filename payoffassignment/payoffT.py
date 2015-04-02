def payoff(B, R, j, inv):
	if(B < 0):
		return(("",float("-inf")))
	if(R < 0):
		return(("",float("-inf")))
	if(j == 0):
		return("",0)
	Pj = inv[1][j-1]
	Cj = inv[0][j-1]
	Rj = inv[2][j-1]
	(stri, none) = payoff(B, R, j-1, inv)
	(strj, some) = payoff(B-Cj, R-Rj, j-1, inv)
	if(none < Pj + some):
		return(str(j) + " " + strj, Pj + some)
	else:
		return(stri, none)

import payoff as p
import payoffT as p2

InvMatrix = [[0 for x in range(7)] for x in range(3)]
InvMatrix[0][0] = 20
InvMatrix[0][1] = 10
InvMatrix[0][2] = 40
InvMatrix[0][3] = 50
InvMatrix[0][4] = 50
InvMatrix[0][5] = 70
InvMatrix[0][6] = 80

InvMatrix[1][0] = 5
InvMatrix[1][1] = 2
InvMatrix[1][2] = 4
InvMatrix[1][3] = 10
InvMatrix[1][4] = 20
InvMatrix[1][5] = 25
InvMatrix[1][6] = 35

InvMatrix[2][0] = 1
InvMatrix[2][1] = 3
InvMatrix[2][2] = 2
InvMatrix[2][3] = 3
InvMatrix[2][4] = 2
InvMatrix[2][5] = 1
InvMatrix[2][6] = 4

memo = {}

B = 140
R = 12
n = 7

(investments, payoff) = p.payoff(B, R, n, InvMatrix,{})
print(investments)
print(payoff)
(investments, payoff) = p2.payoff(B, R, n, InvMatrix)
print(investments)
print(payoff)

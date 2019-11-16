import random
import math

def next_bridge_3(p, s):
	n, k = p[0], p[1]
	i = k % (2 * s)
	a = int(n - (1/2) + (1/2)*math.pow(-1, n + k))
	b = (i//2) % s
	return (a, b)

def find_bridge_prob_2(nb, Po):
	if nb in b:
		return b[nb]
	b[nb] = (random.randrange(100) , (Po * 100))
	return b[nb]

def move_2(p, s, P):
	nb = next_bridge_3(p, s)
	if find_bridge_prob_2(nb, P):
		if p[0] == nb[0]
			np = (p[0] + 1, (p[1] + 1) % (2 * s))
		elif p[0] == nb[0] + 1:
			np = (p[0] - 1, (p[1] + 1) % (2 * s))
	if not find_bridge_prob_2(nb, P):
		np = (p[0], (p[1] + 1) % (2 * s))
	return np

N = 100000
S = 2
P = 0.5

E = 0

for i in range(N):
	b = {}
	pv = []
	pi = (0, 0)
	p = (0, 0)
	while pi not in pv:
		p = move_2(p, S, P)
		pv.append(p)
	E += len(pv)

print("The average number of loops is {}".format(E / (2 * S * N)))
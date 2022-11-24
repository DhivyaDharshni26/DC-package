import math


def Elias_Delta_Decoding(x):
	x = list(x)
	L = 0
	while True:
		if not x[L] == '0':
			break
		L = L + 1
		
	# Reading L more bits and dropping ALL	
	x = x[2*L+1:]
	
	# Prepending with 1 in MSB
	x.reverse()
	x.insert(0, '1')
	n = 0
	
	# Converting binary to integer
	for i in range(len(x)):
		if x[i] == '1':
			n = n+math.pow(2, i)
	return int(n)


x = '01111'
print(Elias_Delta_Decoding(x))
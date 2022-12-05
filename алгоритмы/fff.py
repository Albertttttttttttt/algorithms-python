def stopapupa(n):
	bum = 0
	while n > 4:
		if n % 8:
			n = n // 4 + 8
			bum += n - 1
		else:
			n //= 8
			bum += n
	return bum

print(stopapupa(int(input())))
def fibo(n):
	return fibo(n-1)+fibo(n-2) if n >=2 else n

	for n in range(1,11):
		print(n, fibo(n))

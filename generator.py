import random

def fmp(b,p,m):
	res=1
	while p>0:
		if p%2==1:
			res = res*b%m
		p>>=1
		b=b*b%m
	return res

def isPrime(n, k):
	if n==1 or n==4:
		return False
	if n==2 or n==3:
		return True
	for i in range(k):
		a = random.randint(2, n-2)
		if fmp(a,n-1,n) != 1:
		#	print("Not prime")
			return False
	print("Prime!")
	return True

def genPrime(lo):
	if lo%2==0:
		lo+=1
	while isPrime(lo, 1000)==False:
		lo+=2
	return lo

p=genPrime(random.randint(1<<1022,1<<1023))
q=genPrime(random.randint(1<<1022,1<<1023))
e=65537
n=p*q
et = (p-1)*(q-1)

print("p: "+str(p))
print("q: "+str(q))
print("n: "+str(n))
print("e: "+str(e))
print("et: "+str(et))
m = "Number Theory is Fun!"
pt = 0
for i in m:
	pt=pt*1000+ord(i)	
print("pt: "+str(pt))
ct = fmp(pt,e,n)
print("ct: " + str(ct))



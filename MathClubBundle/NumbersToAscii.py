import sys

pt = str(sys.argv[1])
res = ""

i=len(pt)-1
while i>=0:
	c=""
	j=0
	while j<3 and i-j>=0:
		c=pt[i-j:i-j+1]+c
		j+=1
	res=str(chr(int(c)))+res
	i-=3

print(res)

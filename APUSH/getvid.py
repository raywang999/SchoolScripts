import urllib.request

def ftot(f):
	i=int(f)
	return str(int(i/3600))+":"+str(int((i%3600)/60))+":"+str(int(i%60))

file = open('playlist.m3u8','r')
data = file.read().split('\n')
currt = 0.0
prevt=0
for i in data:
	if (i[0:8]=="#EXTINF:"):
		prevt=float(i[8:16])
		print(currt)
	elif (i[0:5]=="https"):
		filename=ftot(currt)+".ts"
		try:
			f=open(filename)
			print(filename)
		except:
			urllib.request.urlretrieve(i,filename)
		currt+=prevt
		

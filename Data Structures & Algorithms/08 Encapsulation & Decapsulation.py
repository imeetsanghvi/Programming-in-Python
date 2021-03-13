def encap(header, string):
    	newstring = header + string
	return newstring

def decap(header, string):
	string =  string.replace(header,"")
	return string

string, nheader = input('enter string & number of headers you want to enter seperated by space:\n').split(" ")
nheader = int(nheader)
nh = [0]*nheader
print("enter the headerss: ", str(nheader))
for i in range(0,nheader):
	nh[i] = input()
flag = 0
max1 = len(nh[0])
for i in range(0,nheader):
	if max1 < len(nh[i]):
		max1 = len(nh[i])
		print(max1)
for i in range(0,nheader):
	if len(nh[i])!=max1:					flag = 1
if flag != 1: 									print("\nthe type is IP in IP")
else: 		    									print("\nthe type is generic")
print("\n\nencapsulating")
for i in range(0,nheader):
	string = encap(nh[i], string)
print(string)
print("\n\ndecapsulating")
for i in range(0,nheader):
	string = decap(nh[i], string)
print(string)
a = int (input("nhap n: "))
s = 0
for i in range(1,a+1):
 	print i
for i in range(1,a+1):
	if(i%2==0):
		s = s+i
print ("Tong cac so chan:"),s

# Exam
#Oscar Eduardo Sanchez
x1=int(input("Dame su valor: "))
y1=int(input("Dame su valor: "))
x2=int(input("Dame su valor: "))
y2=int(input("Dame su valor: "))

def distancia(a,b,c,d):
	t1=c-a
	t2=d-b
	t1=t1*t1
	t2=t2*t2
	t3=t1+t2
	t= math.sqrt(t3)
		
	return t
T=distancia(a,b,c,d)
print (T)

import array as ar
import numpy as np
import matplotlib.pyplot as plt 

X1=[1,1,0,0]
X2=[1,0,1,0]
W1=[0]
W2=[0]
bias=1
b=[0]
y=[]
Delta_w1=[]
Delta_w2=[]
Delta_b=[]

def OR(n1,n2):
	n=[]
	for x in range(0,4):
		if n1[x]==0 and n2[x]==0 : n.append(0)
		else:  n.append(1)
	return n


def Bigolar(y):
	temp=[]
	for x in range(0,4):
		if y[x]==0: 
			temp.append(-1)
		else: 
			temp.append(1)
	return temp


def Line(x,y):
	z=[-1,1]
	eq=[]
	eq.append(x*z[0]+y)
	eq.append(x*z[1]+y)
	return z,eq



y=OR(X1,X2)
print("binary result: ",y)
t=Bigolar(y)
print("Bigolar result: ",t)
for i in range(0,4):
	Delta_w1.append(X1[i]*t[i])
	Delta_w2.append(X2[i]*t[i])
	Delta_b.append(1*t[i])

for j in range(0,4):
	W1.append(W1[j]+Delta_w1[j])
	W2.append(W2[j]+Delta_w2[j])
	b.append(b[j]+Delta_b[j])

W1.pop(0)
W2.pop(0)
b.pop(0)
print("Delta_w1: ",Delta_w1)
print("Delta_w2: ",Delta_w2)
print("Delta_b: ",Delta_b)
print("W1: ",W1)
print("W2: ",W2)
print("b: ",b)



a=[]
c=[]

for d in range(0,4):
	a.append(-W1[d]/W2[d])
	c.append(-b[d]/W2[d])


col=[]
for i in range(0, 4):
    if X1[i]==0 and X2[i]==0:
        col.append('red')  
    else:
        col.append('blue') 
plt.scatter(1, 1, c = 'blue', s = 10,linewidth = 5)
plt.scatter(1, -1, c = 'blue', s = 10,linewidth = 5)
plt.scatter(-1, 1, c = 'blue', s = 10,linewidth = 5)
plt.scatter(-1, -1, c = 'red', s = 10,linewidth = 5)
for i in range(0,4):
	d,e=Line(a[i],c[i])
	plt.plot(d, e, color='purple')	
plt.show()
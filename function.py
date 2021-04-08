from random import random
import math
import turtle as t
#from time import clock
def  drawpi(Darts):
	# Darts=10000
	hits = 0.0
	#clock()
	drawframe(1)
	t.tracer(False)
	t.penup()
	for i in  range(1,Darts+1):
		x,y = random(),random()
		t.goto(x*300,y*300)
		dist=math.sqrt(x**2+y**2)
		if dist<1.0:
			hits=hits+1
			t.dot(3,"red")
		else:
			t.dot(3,"blue")
	pi=4*(hits/Darts)
	print("Pi is {}".format(pi))
	t.tracer(True)
	t.done()
	# pi=4*(hits/Darts)
	# print("Pi is {}".format(pi))
#drawpi(5000)
def drawframe(len):
	t.penup()
	t.goto(0,0)
	t.seth(90)
	t.pendown()
	t.forward(len*300)
	t.seth(0)
	t.circle(-len*300,90)
	t.seth(180)
	t.forward(len*300)
	t.goto(0,len*300)
	# t.pendown()
	t.seth(0)
	t.forward(300*len)
	t.seth(-90)
	t.forward(300*len)
# drawframe(1)
# drawframe(1)
def isPrime(number):
	for i in range(2,number//2+1):
		if number%i!=0:
			continue
		else:
			return False
	return True

def FindBigPrime(number):
	for i in range(number,1,-1):
		if isPrime(i):
			# print(i)
			return i 

# a=eval(input("Please input a number:"))
# print(FindBigPrime(a))	
# a=eval(input())
# if isPrime(a):
# 	print("yes")
# else:
# 	print("no")

if __name__=='__main__':
	#number=eval(input("Please input a number:"))
	#x= lambda number : "" if isPrime(number) else "not"
	print("{} is the biggest prime number".format(FindBigPrime(5000)))
	a=FindBigPrime(5000)
	# print(a)
	drawpi(a)
	#print("{} is {} a Prime number".format(number,x(number)))
import os
from termcolor import *
o_f = open("main.txt", "a")
z = 2
Anish = open("main.txt")

print(colored("1.add member\n\n2.delete member\n","yellow"))

li=[]
def deli():
	din = input("enter number which you want remove?\n:")
for item in Anish:
	lll = len(item)
	#print(lll)
	z = z+1
	print(f"{z}.{item}")
	li.append(item[0:lll-1])
iurt = colored("enter number?\n:","green")
inp = input(iurt)
if inp=="2":
	deli()
if inp=="1":
	adm = input("enter name\n: ","green")
	admm = int(input("enter if any amount?\n:"))
	o_f.write(f"{adm}\n")
	mo = open(f"{adm}.txt", "w")
	mo.write(f"{admm}")
o_f.close()
Anish.close()
print(li)
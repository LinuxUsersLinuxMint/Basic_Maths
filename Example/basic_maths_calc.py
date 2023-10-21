#!/usr/bin/python3
# Basic_Maths ile yapılmış bir calcutator programıdır. (Basic_Maths) kullanımına örnek olması amaçlı yazılmıştır.

from Basic_Maths import *
number1=int(input('N1: '))
number2=int(input('N2: '))
select=str(input('Select (Add, Ext, Mul, Div, Per, FullDiv, TakeEx): '))

if select=="Add":
    addition(number1,number2)
elif select=="Ext":
    Extraction(number1,number2)
elif select=="Mul":
    Multiplication(number1,number2)
elif select=="Div":
    Division(number1,number2)
elif select=="Per":
    Percentage(number1,number2)
elif select=="FullDiv":
    FullDivision(number1,number2)
elif select=="TakeEx":
    TakingExponents(number1,number2)
else:
    print("Invalid Process...!")

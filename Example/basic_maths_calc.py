#!/usr/bin/python3
# Basic_Maths ile yapılmış bir calcutator programıdır. (Basic_Maths) kullanımına örnek olması amaçlı yazılmıştır.
# It is a calculator program made with Basic_Maths. It was written to serve as an example of (Basic_Maths) usage.

from Basic_Maths import *
number1=int(input('N1: '))
number2=int(input('N2: '))
select=str(input('Select (Add, Ext, Mul, Div, Per, FullDiv, TakeEx): '))

resultdialog = str("Result:")

if select=="Add":
    addition(number1,number2,resultdialog)
elif select=="Ext":
    Extraction(number1,number2,resultdialog)
elif select=="Mul":
    Multiplication(number1,number2,resultdialog)
elif select=="Div":
    Division(number1,number2,resultdialog)
elif select=="Per":
    Percentage(number1,number2,resultdialog)
elif select=="FullDiv":
    FullDivision(number1,number2,resultdialog)
elif select=="TakeEx":
    TakingExponents(number1,number2,resultdialog)
else:
    print("Invalid Process...!")
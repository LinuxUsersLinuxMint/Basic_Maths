#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/Basic_Maths
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/Basic_Maths"""

from library_func import *

global result

select_func = str()
"""
Example:

input_select = str(input('Which process?'))
select_func = input_select

def addition(x,y,ResultDialog):
    result=x+y
    print("{0} {1} {2} + {3} = {4}". format(select_func,ResultDialog,x,y,result))

"""

def addition(x,y,ResultDialog):
    result=x+y
    print("{0} {1} {2} + {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Extraction(x,y,ResultDialog):
    result=x-y
    print("{0} {1} {2} - {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Multiplication(x,y,ResultDialog):
    result=x*y
    print("{0} {1} {2} * {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Division(x,y,ResultDialog):
    if y==0:
        print("The second number cannot be zero in division!")
    if y>0:
        result=x/y
        print("{0} {1} {2} / {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Percentage(x,y,ResultDialog):
    result=x%y
    print("{0} {1} {2} % {3} = {4}". format(select_func,ResultDialog,x,y,result))

def FullDivision(x,y,ResultDialog):
    result=x//y
    print("{0} {1} {2} // {3} = {4}". format(select_func,ResultDialog,x,y,result))

def TakingExponents(x,y,ResultDialog):
    result=x ** y
    print("{0} {1} {2} ** {3} = {4}". format(select_func,ResultDialog,x,y,result))

def TakingRoots(x,y,ResultDialog):
    result=x ** (1/y)
    print("{0} {1} {2} / (1/y) = {3}". format(select_func,ResultDialog,x,result))

def SqaureRoot(x,ResultDialog):
    result=x ** (1/2)
    print("{0} {1} {2} ** (1/2) = {3}". format(select_func,ResultDialog,x,result))

#!/usr/bin/python3
"""Copyright© 2023-2024 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"""

global result

PYTHON_LIB_LICENCE="GPL2"
PYTHON_LIB_VER="2.0"
PYTHON_LIB_AUTHOR="LinuxUsersLinuxMint"

def addition(x,y,ResultDialog):
    x=x
    y=y
    result=x+y
    print("{0} {1} + {2} = {3}". format(ResultDialog,x,y,result))
def Extraction(x,y,ResultDialog):
    x=x
    y=y
    result=x-y
    print("{0} {1} - {2} = {3}". format(ResultDialog,x,y,result))
def Multiplication(x,y,ResultDialog):
    x=x
    y=y
    result=x*y
    print("{0} {1} * {2} = {3}". format(ResultDialog,x,y,result))
def Division(x,y,ResultDialog):
    x=x
    y=y
    if y=0:
        print("The second number cannot be zero in division!")
    if y>0:
        result=x/y
        print("{0} {1} / {2} = {3}". format(ResultDialog,x,y,result))
def Percentage(x,y,ResultDialog):
    x=x
    y=y
    result=x%y
    print("{0} {1} % {2} = {3}". format(ResultDialog,x,y,result))
def FullDivision(x,y,ResultDialog):
    x=x
    y=y
    result=x//y
    print("{0} {1} // {2} = {3}". format(ResultDialog,x,y,result))
def TakingExponents(x,y,ResultDialog):
    x=x
    y=y
    result=x ** y
    print("{0} {1} ** {2} = {3}". format(ResultDialog,x,y,result))
def TakingRoots(x,y,ResultDialog):
    x=x
    y=y
    result=x ** (1/y)
    print("{0} {1} / (1/y) = {2}". format(ResultDialog,x,result))
def SqaureRoot(x,ResultDialog):
    x=x
    result=x ** (1/2)
    print("{0} {1} ** (1/2) = {2}". format(ResultDialog,x,result))
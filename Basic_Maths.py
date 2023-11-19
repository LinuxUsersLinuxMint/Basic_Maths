#!/usr/bin/python3
"""Copyright© 2023 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"""

def addition(x,y,ResultDialog):
    x=x
    y=y
    global result
    result=x+y
    print("{3} {0} + {1} = {2}". format(x,y,result,ResultDialog))
def Extraction(x,y,ResultDialog):
    x=x
    y=y
    global result
    result=x-y
    print("{3} {0} - {1} = {2}". format(x,y,result,ResultDialog))
def Multiplication(x,y,ResultDialog):
    x=x
    y=y
    global result
    result=x*y
    print("{3} {0} * {1} = {2}". format(x,y,result,ResultDialog))
def Division(x,y,ResultDialog):
    x=x
    y=y
    global result
    result=x/y
    print("{3} {0} / {1} = {2}". format(x,y,result,ResultDialog))
def Percentage(x,y,ResultDialog):
    x=x
    y=y
    global result
    result=x%y
    print("{3} {0} % {1} = {2}". format(x,y,result,ResultDialog))
def FullDivision(x,y,ResultDialog):
    x=x
    y=y
    global result
    result=x//y
    print("{3} {0} // {1} = {2}". format(x,y,result,ResultDialog))
def TakingExponents(x,y,ResultDialog):
    x=x
    y=y
    global result
    result=x ** y
    print("{3} {0} ** {1} = {2}". format(x,y,result,ResultDialog))
def TakingRoots(x,y,ResultDialog):
    x=x
    y=y
    global result
    result=x ** (1/y)
    print("{3} {0} ** (1/{1}) = {2}". format(x,y,result,ResultDialog))
def SqaureRoot(x):
    x=x
    global result
    result=x ** (1/2)
    print("{3} {0} ** (1/2) = {1}". format(x,result,ResultDialog))

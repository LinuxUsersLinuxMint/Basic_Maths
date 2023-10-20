#!/usr/bin/python3
"Copyright© 2023 LinuxUsersLinuxMint"
"Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Basic_Maths All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

def addition(x,y):
    x=x
    y=y
    global result
    result=x+y
    print("result: {0} + {1} = {2}". format(x,y,result))
def Extraction(x,y):
    x=x
    y=y
    global result
    result=x-y
    print("result: {0} - {1} = {2}". format(x,y,result))
def Multiplication(x,y):
    x=x
    y=y
    global result
    result=x*y
    print("result: {0} * {1} = {2}". format(x,y,result))
def Division(x,y):
    x=x
    y=y
    global result
    result=x/y
    print("result: {0} / {1} = {2}". format(x,y,result))
def Percentage(x,y):
    x=x
    y=y
    global result
    result=x%y
    print("result: {0} % {1} = {2}". format(x,y,result))
def FullDivision(x,y):
    x=x
    y=y
    global result
    result=x//y
    print("result: {0} // {1} = {2}". format(x,y,result))
def TakingExponents(x,y):
    x=x
    y=y
    global result
    result=x ** y
    print("result {0} ** {1} = {2}". format(x,y,result))
def TakingRoots(x,y):
    x=x
    y=y
    global result
    result=x ** (1/y)
    print("result: {0} ** (1/{1}) = {2}". format(x,y,result))
def SqaureRoot(x):
    x=x
    global result
    result=x ** (1/2)
    print("result: {0} ** (1/2) = {1}". format(x,result))
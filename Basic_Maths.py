#!/usr/bin/python3
"""Copyright© 2023-2024 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"""

global result

PYTHON_LIB_NAME="Basic_Maths"
PYTHON_LIB_LICENCE="GPL2"
PYTHON_LIB_VER="2.1"
PYTHON_LIB_AUTHOR="LinuxUsersLinuxMint"

# Math functions

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


# Library functions

def LibAbout():
    print("Python Library Name: {0}", format(PYTHON_LIB_NAME))
    print("Python Library Version: {0}\n", format(PYTHON_LIB_VER))
    print("Python Library Licence Name: {0}\n", format(PYTHON_LIB_LICENCE))
    print("Python Library Author Name: {0}\n", format(PYTHON_LIB_AUTHOR))

# TR (Türkçe):
# NOT: "Kütüphane fonksiyonları" başlığı altındaki fonksiyonlar kullanımı isteğe bağlıdır ancak "Basic_Maths" kütüphanesini kullanan bir "Python" yazılımında kullanıcıya kullanılan kütüphane hakkında bilgi vermek amacıyla kullanılabilir.

# EN (English):
# NOTE: The functions under the "Library functions" heading are optional, but can be used in a "Python" software that uses the "Basic_Maths" library to provide information to the user about the library used.
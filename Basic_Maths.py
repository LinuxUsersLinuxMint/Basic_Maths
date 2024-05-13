#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/Basic_Maths
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/Basic_Maths"""

global result

PYTHON_LIB_NAME="Basic_Maths"
PYTHON_LIB_LICENCE="GPL2"
PYTHON_LIB_VER="2.5"
PYTHON_LIB_AUTHOR="LinuxUsersLinuxMint"

# Math functions

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

#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/Basic_Maths
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/Basic_Maths"""

from math import *
from PyAppDevKit.LibFunc.pyappdevkit import *
from Basic_Maths.lib_ver_info import *
from Basic_Maths.library_func import *

""" TR (Turkish / Türkçe):
NOT: InputN1N2() sadece 2 sayının istendiği durumlarda kullanılabilir.

EN (English / İngilizce):
NOTE: InputN1N2() can be used when only 2 numbers are required. """

def InputN1N2(number_one_dialog,number_two_dialog):
    global number_one, number_two
    number_one = float(input("{0}". format(number_one_dialog)))
    number_two = float(input("{0}". format(number_two_dialog)))

select_func = str()
"""
Example:

input_select = str(input('Which process?'))
select_func = input_select

def Addition(x,y,ResultDialog):
    result=x+y
    print("{0} {1} {2} + {3} = {4}". format(select_func,ResultDialog,x,y,result))

"""

def Addition(x,y,ResultDialog):
    result=x+y
    print("{0} {1} {2} + {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Extraction(x,y,ResultDialog):
    result=x-y
    print("{0} {1} {2} - {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Multiplication(x,y,ResultDialog):
    result=x*y
    print("{0} {1} {2} * {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Division(x,y,ResultDialog,check_zero_control_msg):
    if x==0 or y==0:
        print(check_zero_control_msg)
    if y>0 and x>0:
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
    print("{0} {1} {2} / (1/{3}) = {4}". format(select_func,ResultDialog,x,y,result))

def SqaureRoot(x,ResultDialog):
    result=x ** (1/2)
    print("{0} {1} {2} ** (1/2) = {3}". format(select_func,ResultDialog,x,result))

""" TR (Turkish / Türkçe):
NOT: "Basic_Maths" kütüphanesini kullanan geliştiriciler programlarındaki ihtiyaçlara göre "Basic_Maths" fonksiyonlarını değiştirebilirler.
NOT2: "select_process" değişkeni ile geliştiriciler isteğe bağlı olarak programlarında kullanıcılar tarafından seçilen işlemi gösterebilir.
NOT3: "nod" ve "ntd" değişkenleri ile beraber geliştiriciler "all_math_operations()" fonksiyonunda "InputN1N2()" fonksiyonunu kullanabilir ve bu değişkenler aracılığıyla 1. sayı ve 2. sayı diyaloglarını ekleyebilirler.
ÖNERİ: Eğer istekleriniz veya ihtiyaçlarınız farklıysa "all_math_operations()" fonksiyonunu kullanmadan önce ihtiyaçlarınız doğrultusunda değiştirmeniz önerilir. 

EN (English / İngilizce):
NOTE: Developers using the "Basic_Maths" library can change the "Basic_Maths" functions according to the needs of their programs.
NOTE2: With the "select_process" variable, developers can optionally display the process selected by users in their programs.
NOTE3: Along with the "nod" and "ntd" variables, developers can use the "InputN1N2()" function in the "all_math_operations()" function and add the 1st issue and 2nd issue dialogs through these variables.
SUGGESTION: If your wishes or needs are different, it is recommended that you change it according to your needs before using the "all_math_operations()" function. """

def all_math_operations(optDialog,first_opt_dialog,second_opt_dialog,third_opt_dialog,fourth_opt_dialog,fifth_opt_dialog,sixth_opt_dialog,seventh_opt_dialog,eighth_opt_dialog,ninth_opt_dialog,SelectOptDialog,nod,ntd,resdialog,divisionzerocheckdialog,errdg):
    print(optDialog)
    print(first_opt_dialog)
    print(second_opt_dialog)
    print(third_opt_dialog)
    print(fourth_opt_dialog)
    print(fifth_opt_dialog)
    print(sixth_opt_dialog)
    print(seventh_opt_dialog)
    print(eighth_opt_dialog)
    print(ninth_opt_dialog)
    select_func = str(input(SelectOptDialog))
    InputN1N2(nod,ntd)
    if select_func == "1" or select_func == "Addition" or select_func == "Toplama":
        Addition(number_one,number_two,resdialog)
    elif select_func == "2" or select_func == "Extraction" or select_func == "Çıkarma":
        Extraction(number_one,number_two,resdialog)
    elif select_func == "3" or select_func == "Multiplication" or select_func == "Çarpma":
        Multiplication(number_one,number_two,resdialog)
    elif select_func == "4" or select_func == "Division" or select_func == "Bölme":
        Division(number_one,number_two,resdialog,divisionzerocheckdialog)
    elif select_func == "5" or select_func == "Percentage" or select_func == "Yüzdelik":
        Percentage(number_one,number_two,resdialog)
    elif select_func == "6" or select_func == "FullDivision" or select_func == "Tam bölüm":
        FullDivision(number_one,number_two,resdialog)
    elif select_func == "7" or select_func == "TakingExponents" or select_func == "Üslü sayı alma":
        TakingExponents(number_one,number_two,resdialog)
    elif select_func == "8" or select_func == "TakingRoots" or select_func == "Kök Alma":
        TakingRoots(number_one,number_two,resdialog)
    elif select_func == "9" or select_func == "SquareRoot" or select_func == "Kare kök":
        SqaureRoot(number_one,resdialog)
    else:
        error_msg(errdg)
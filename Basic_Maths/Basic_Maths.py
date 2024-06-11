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

def all_math_operations(optDialog,first_opt_dialog,second_opt_dialog,third_opt_dialog,fourth_opt_dialog,fifth_opt_dialog,sixth_opt_dialog,seventh_opt_dialog,eighth_opt_dialog,ninth_opt_dialog,SelectOptDialog,nod,ntd,resdialog,divisionzerocheckdialog,errdg,addition_options_one,addition_options_two,addition_options_three,addition_options_four,addition_options_five,extraction_options_one,extraction_options_two,extraction_options_three,extraction_options_four,extraction_options_five,multiplication_options_one,multiplication_options_two,multiplication_options_three,multiplication_options_four,multiplication_options_five,division_options_one,division_options_two,division_options_three,division_options_four,division_options_five,percentage_options_one,percentage_options_two,percentage_options_three,percentage_options_four,percentage_options_five,fulldivision_options_one,fulldivision_options_two,fulldivision_options_three,fulldivision_options_four,fulldivision_options_five,takingexponents_options_one,takingexponents_options_two,takingexponents_options_three,takingexponents_options_four,takingexponents_options_five,takingroots_options_one,takingroots_options_two,takingroots_options_three,takingroots_options_four,takingroots_options_five,squareroot_options_one,squareroot_options_two,squareroot_options_three,squareroot_options_four,squareroot_options_five):
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
    if select_func == addition_options_one or select_func == addition_options_two or select_func == addition_options_three or select_func == addition_options_four or select_func == addition_options_five:
        Addition(number_one,number_two,resdialog)
    elif select_func == extraction_options_one or select_func == extraction_options_two or select_func == extraction_options_three or select_func == extraction_options_four or select_func == extraction_options_five:
        Extraction(number_one,number_two,resdialog)
    elif select_func == multiplication_options_one or select_func == multiplication_options_two or select_func == multiplication_options_three or select_func == multiplication_options_four or select_func == multiplication_options_five:
        Multiplication(number_one,number_two,resdialog)
    elif select_func == division_options_one or select_func == division_options_two or select_func == division_options_three or select_func == division_options_four or select_func == division_options_five:
        Division(number_one,number_two,resdialog,divisionzerocheckdialog)
    elif select_func == percentage_options_one or select_func == percentage_options_two or select_func == percentage_options_three or select_func == percentage_options_four or select_func == percentage_options_five:
        Percentage(number_one,number_two,resdialog)
    elif select_func == fulldivision_options_one or select_func == fulldivision_options_two or select_func == fulldivision_options_three or select_func == fulldivision_options_four or select_func == fulldivision_options_five:
        FullDivision(number_one,number_two,resdialog)
    elif select_func == takingexponents_options_one or select_func == takingexponents_options_two or select_func == takingexponents_options_three or select_func == takingexponents_options_four or select_func == takingexponents_options_five:
        TakingExponents(number_one,number_two,resdialog)
    elif select_func == takingroots_options_one or select_func == takingroots_options_two or select_func == takingroots_options_three or select_func == takingroots_options_four or select_func == takingroots_options_five:
        TakingRoots(number_one,number_two,resdialog)
    elif select_func == squareroot_options_one or select_func == squareroot_options_two or select_func == squareroot_options_three or select_func == squareroot_options_four or select_func == squareroot_options_five:
        SqaureRoot(number_one,resdialog) 
    else:
        error_msg(errdg)
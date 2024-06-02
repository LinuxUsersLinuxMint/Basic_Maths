#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/Basic_Maths
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/Basic_Maths"""

import time

PYTHON_LIB_NAME="Basic_Maths"
PYTHON_LIB_LICENCE="GPL2"
PYTHON_LIB_VER="3.7re-edit"
PYTHON_LIB_SUPPORT_PLATFORM="Windows/Linux/macOS/otherOS"
PYTHON_LIB_RELEASE_DATE="9/30/2023, Time: XX:XX"
PYTHON_LIB_LAST_UPDATE_DATE="6/2/2024, Time: 21:55"
PYTHON_LIB_AUTHOR="LinuxUsersLinuxMint"
PYTHON_LIB_AUTHOR_WEB_SITE="https://linuxuserslinuxmint.github.io"

def LibAbout():
    print("Python Library Name:", format(PYTHON_LIB_NAME))
    print("Python Library Version:", format(PYTHON_LIB_VER))
    print("Python Library Support OS:", format(PYTHON_LIB_SUPPORT_PLATFORM))
    print("Python Library Licence Name:", format(PYTHON_LIB_LICENCE))
    print("Python Library Author Name:", format(PYTHON_LIB_AUTHOR))
    print("Python Library Author Web Site:", format(PYTHON_LIB_AUTHOR_WEB_SITE))
    print("Python Library Release Date:", format(PYTHON_LIB_RELEASE_DATE))
    print("Python Library Last Update Date:", format(PYTHON_LIB_LAST_UPDATE_DATE))

error_dialog = str()

def error_msg():
    print(error_dialog)

def exit_program_dialog_time(exit_dialog_msg,userTime):
    print(exit_dialog_msg)
    userTime = int(userTime)
    time.sleep(userTime)
    exit()

def exit_program_time(userTime):
    time.sleep(userTime)
    userTime = int(userTime)
    exit()

def exit_program_dialog(exit_dialog_msg):
    print(exit_dialog_msg)
    exit()

""" Example Dialog (ExitSelectDialog): "Select the method to exit the program (0: Dialogue and Time entry, 1: Time entry only, 2: Dialogue entry only, 3: Normal exit (old style)): "
# Example Dialog (userTimeDialog): "After how many seconds should the program be closed?: "
# Example Dialog (exitDialog): "Exit program..."
# Example Dialog (errormsgDialog): "Invalid Command!" """

def all_exit(ExitSelectDialog,userTimeDialog,exitDialog,errormsgDialog):
    exit_select = int(input(ExitSelectDialog))
    exit_select = int(exit_select)
    if exit_select == 0:
        userTime = input(userTimeDialog)
        exit_program_dialog_time(exitDialog, userTime)
    elif exit_select == 1:
        userTime = input(userTime)
        exit_program_time(userTime)
    elif exit_select == 2:
        exit_program_dialog(exitDialog)
    elif exit_select == 3:
        exit()
    else:
        print(errormsgDialog)

def program_welcome_msg(welcome_msg):
    print(welcome_msg)

def program_info(programnamedialog,program_name,programversiondialog,program_version,programsupportosdialog,program_support_os,programlicencedialog,program_licence,programauthordialog,program_author,programauthorwebsitedialog,program_author_web_site,programreleasedatedialog,program_rs_date,programlastupdatedatedialog,program_last_update_date):
    print("{0} {1}". format(programnamedialog,program_name))
    print("{0} {1}". format(programversiondialog,program_version))
    print("{0} {1}". format(programsupportosdialog,program_support_os))
    print("{0} {1}". format(programlicencedialog,program_licence))
    print("{0} {1}". format(programauthordialog,program_author))
    print("{0} {1}". format(programauthorwebsitedialog,program_author_web_site))
    print("{0} {1}". format(programreleasedatedialog,program_rs_date))
    print("{0} {1}". format(programlastupdatedatedialog,program_last_update_date))

# TR (Turkish / Türkçe):
# NOT: InputN1N2() sadece 2 sayının istendiği durumlarda kullanılabilir.
# EN (English / İngilizce):
# NOTE: InputN1N2() can be used when only 2 numbers are required.

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
    print("{0} {1} {2} / (1/y) = {3}". format(select_func,ResultDialog,x,result))

def SqaureRoot(x,ResultDialog):
    result=x ** (1/2)
    print("{0} {1} {2} ** (1/2) = {3}". format(select_func,ResultDialog,x,result))

# TR (Turkish / Türkçe):
# NOT: "Basic_Maths" kütüphanesini kullanan geliştiriciler programlarındaki ihtiyaçlara göre "Basic_Maths" fonksiyonlarını değiştirebilirler.
# NOT2: "select_process" değişkeni ile geliştiriciler isteğe bağlı olarak programlarında kullanıcılar tarafından seçilen işlemi gösterebilir.
# NOT3: "nod" ve "ntd" değişkenleri ile beraber geliştiriciler "all_math_operations()" fonksiyonunda "InputN1N2()" fonksiyonunu kullanabilir ve bu değişkenler aracılığıyla 1. sayı ve 2. sayı diyaloglarını ekleyebilirler.
# ÖNERİ: Eğer istekleriniz veya ihtiyaçlarınız farklıysa "all_math_operations()" fonksiyonunu kullanmadan önce ihtiyaçlarınız doğrultusunda değiştirmeniz önerilir.

# EN (English / İngilizce):
# NOTE: Developers using the "Basic_Maths" library can change the "Basic_Maths" functions according to the needs of their programs.
# NOTE2: With the "select_process" variable, developers can optionally display the process selected by users in their programs.
# NOTE3: Along with the "nod" and "ntd" variables, developers can use the "InputN1N2()" function in the "all_math_operations()" function and add the 1st issue and 2nd issue dialogs through these variables.
# SUGGESTION: If your wishes or needs are different, it is recommended that you change it according to your needs before using the "all_math_operations()" function.

def all_math_operations(optDialog,first_opt_dialog,second_opt_dialog,third_opt_dialog,fourth_opt_dialog,fifth_opt_dialog,sixth_opt_dialog,seventh_opt_dialog,eighth_opt_dialog,ninth_opt_dialog,SelectOptDialog,nod,ntd,resdialog,divisionzerocheckdialog,errdg):
    error_dialog = errdg
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
    select_opt = str(input(SelectOptDialog))
    select_process=select_opt
    InputN1N2(nod,ntd)
    if select_opt == "1":
        Addition(number_one,number_two,resdialog)
    elif select_opt == "2":
        Extraction(number_one,number_two,resdialog)
    elif select_opt == "3":
        Multiplication(number_one,number_two,resdialog)
    elif select_opt == "4":
        Division(number_one,number_two,resdialog,divisionzerocheckdialog)
    elif select_opt == "5":
        Percentage(number_one,number_two,resdialog)
    elif select_opt == "6":
        FullDivision(number_one,number_two,resdialog)
    elif select_opt == "7":
        TakingExponents(number_one,number_two,resdialog)
    elif select_opt == "8":
        TakingRoots(number_one,number_two,resdialog)
    elif select_opt == "9":
        SqaureRoot(number_one,resdialog)
    else:
        error_msg()
#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/Basic_Maths
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/Basic_Maths"""

from Basic_Maths.library_func import *
import time

global result,error_dialog

error_dialog = str()

def error_msg():
    p(error_dialog)

def exit_program_dialog_time(exit_dialog_msg,userTime):
    p(exit_dialog_msg)
    userTime = int(userTime)
    time.sleep(userTime)
    exit()

def exit_program_time(userTime):
    time.sleep(userTime)
    userTime = int(userTime)
    exit()

def exit_program_dialog(exit_dialog_msg):
    p(exit_dialog_msg)
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
        p(errormsgDialog)

def program_welcome_msg(welcome_msg):
    p(welcome_msg)

def program_info(programnamedialog,program_name,programversiondialog,program_version,programsupportosdialog,program_support_os,programlicencedialog,program_licence,programauthordialog,program_author,programauthorwebsitedialog,program_author_web_site,programreleasedatedialog,program_rs_date,programlastupdatedatedialog,program_last_update_date):
    p("{0} {1}". format(programnamedialog,program_name))
    p("{0} {1}". format(programversiondialog,program_version))
    p("{0} {1}". format(programsupportosdialog,program_support_os))
    p("{0} {1}". format(programlicencedialog,program_licence))
    p("{0} {1}". format(programauthordialog,program_author))
    p("{0} {1}". format(programauthorwebsitedialog,program_author_web_site))
    p("{0} {1}". format(programreleasedatedialog,program_rs_date))
    p("{0} {1}". format(programlastupdatedatedialog,program_last_update_date))

# TR (Turkish / Türkçe):
# NOT: InputN1N2() sadece 2 sayının istendiği durumlarda kullanılabilir.
# EN (English / İngilizce):
# NOTE: InputN1N2() can be used when only 2 numbers are required.

def InputN1N2(number_one_dialog,number_two_dialog):
    global number_one, number_two
    number_one = str(input("{0}". format(number_one_dialog)))
    number_two = str(input("{0}". format(number_two_dialog)))

select_func = str()
"""
Example:

input_select = str(input('Which process?'))
select_func = input_select

def addition(x,y,ResultDialog):
    result=x+y
    print("{0} {1} {2} + {3} = {4}". format(select_func,ResultDialog,x,y,result))

"""

def Addition(x,y,ResultDialog):
    result=x+y
    p("{0} {1} {2} + {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Extraction(x,y,ResultDialog):
    result=x-y
    p("{0} {1} {2} - {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Multiplication(x,y,ResultDialog):
    result=x*y
    p("{0} {1} {2} * {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Division(x,y,ResultDialog,check_zero_control_msg):
    if x==0 or y==0:
        p(check_zero_control_msg)
    if y>0 and x>0:
        result=x/y
        p("{0} {1} {2} / {3} = {4}". format(select_func,ResultDialog,x,y,result))

def Percentage(x,y,ResultDialog):
    result=x%y
    p("{0} {1} {2} % {3} = {4}". format(select_func,ResultDialog,x,y,result))

def FullDivision(x,y,ResultDialog):
    result=x//y
    p("{0} {1} {2} // {3} = {4}". format(select_func,ResultDialog,x,y,result))

def TakingExponents(x,y,ResultDialog):
    result=x ** y
    p("{0} {1} {2} ** {3} = {4}". format(select_func,ResultDialog,x,y,result))

def TakingRoots(x,y,ResultDialog):
    result=x ** (1/y)
    p("{0} {1} {2} / (1/y) = {3}". format(select_func,ResultDialog,x,result))

def SqaureRoot(x,ResultDialog):
    result=x ** (1/2)
    p("{0} {1} {2} ** (1/2) = {3}". format(select_func,ResultDialog,x,result))

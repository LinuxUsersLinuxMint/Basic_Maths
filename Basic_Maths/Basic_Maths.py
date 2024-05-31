#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/Basic_Maths
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/Basic_Maths"""

from Basic_Maths.library_func import *
import time

global result,input_dialog,error_dialog

input_dialog = str()
error_dialog = str()

def p(userString):
    print(userString)

def error_msg():
    p(error_dialog)

def exit_program_dialog_time(exit_dialog_msg,userTime):
    p(exit_dialog_msg)
    time.sleep(userTime)
    exit()

def exit_program_time(userTime):
    time.sleep(userTime)
    exit()

def exit_program_dialog(exit_dialog_msg):
    p(exit_dialog_msg)
    exit()

def program_welcome_msg(welcome_msg):
    p(welcome_msg)

def program_info(programnamedialog,program_name,programversiondialog,program_version,programsupportosdialog,program_support_os,programlicencedialog,program_licence,programauthordialog,program_author,programreleasedatedialog,program_rs_date):
    p("{0} {1}". format(programnamedialog,program_name))
    p("{0} {1}\n". format(programversiondialog,program_version))
    p("{0} {1}\n". format(programsupportosdialog,program_support_os))
    p("{0} {1}\n". format(programlicencedialog,program_licence))
    p("{0} {1}\n". format(programauthordialog,program_author))
    p("{0} {1}\n". format(programreleasedatedialog,program_rs_date))
    

def InputN1N2():
    global number_one, number_two
    number_one = str(input("{0}". format(input_dialog)))
    number_two = str(input("{0}". format(input_dialog)))

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

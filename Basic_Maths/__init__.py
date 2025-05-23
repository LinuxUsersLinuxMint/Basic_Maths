#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/Basic_Maths
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/Basic_Maths"""

""" TR (Turkish / Türkçe):
NOT: "Basic_Maths" kütüphanesini kullanan geliştiriciler programlarındaki ihtiyaçlara göre "Basic_Maths" fonksiyonlarını değiştirebilirler.
ÖNERİ: Eğer istekleriniz veya ihtiyaçlarınız farklıysa "all_math_operations()" fonksiyonunu kullanmadan önce ihtiyaçlarınız doğrultusunda değiştirmeniz önerilir. 

EN (English / İngilizce):
NOTE: Developers using the "Basic_Maths" library can change the "Basic_Maths" functions according to the needs of their programs.
SUGGESTION: If your wishes or needs are different, it is recommended that you change it according to your needs before using the "all_math_operations()" function. """

from Basic_Maths.Lib.lib import *
from Basic_Maths.Lib.parameters import *

def Addition(x,y,ResultDialog,save_cfg,file_name,save_err_msg):
    print("{0} {1} + {2} = {3}". format(ResultDialog,x,y,x+y))

    if save_cfg == ON:
        file(file_name=file_name,file_mode="a",file_write="{0} {1} + {2} = {3}\n". format(ResultDialog,x,y,x+y))
    elif save_cfg == OFF:
        pass
    elif save_cfg == AUTO:
        file(file_name="history.txt",file_mode="a",file_write="{0} {1} + {2} = {3}\n". format(ResultDialog,x,y,x+y))
    else:
        error_msg(save_err_msg,"","")

def Extraction(x,y,ResultDialog,save_cfg,file_name,save_err_msg):
    print("{0} {1} - {2} = {3}". format(ResultDialog,x,y,x-y))

    if save_cfg == ON:
        file(file_name=file_name,file_mode="a",file_write="{0} {1} - {2} = {3}\n". format(ResultDialog,x,y,x-y))
    elif save_cfg == OFF:
        pass
    elif save_cfg == AUTO:
        file(file_name="history.txt",file_mode="a",file_write="{0} {1} - {2} = {3}\n". format(ResultDialog,x,y,x-y))
    else:
        error_msg(save_err_msg,"","")

def Multiplication(x,y,ResultDialog,save_cfg,file_name,save_err_msg):
    print("{0} {1} * {2} = {3}". format(ResultDialog,x,y,x*y))

    if save_cfg == ON:
        file(file_name=file_name,file_mode="a",file_write="{0} {1} * {2} = {3}\n". format(ResultDialog,x,y,x*y))
    elif save_cfg == OFF:
        pass
    elif save_cfg == AUTO:
        file(file_name="history.txt",file_mode="a",file_write="{0} {1} * {2} = {3}\n". format(ResultDialog,x,y,x*y))
    else:
        error_msg(save_err_msg,"","")

def Division(x,y,ResultDialog,check_zero_msg,save_cfg,file_name,save_err_msg):
    if x==0 or y==0:
        print(check_zero_msg)
    else:
        print("{0} {1} / {2} = {3}". format(ResultDialog,x,y,x/y))
        
        if save_cfg == ON:
            file(file_name=file_name,file_mode="a",file_write="{0} {1} / {2} = {3}\n". format(ResultDialog,x,y,x/y))
        elif save_cfg == OFF:
            pass
        elif save_cfg == AUTO:
            file(file_name="history.txt",file_mode="a",file_write="{0} {1} / {2} = {3}\n". format(ResultDialog,x,y,x/y))
        else:
            error_msg(save_err_msg,"","")

def Percentage(x,y,ResultDialog,save_cfg,file_name,save_err_msg):
      print("{0} ({1} * {2})/100 = {3}". format(ResultDialog,x,y,(x*y)/100))

      if save_cfg == ON:
        file(file_name=file_name,file_mode="a",file_write="{0} ({1} * {2})/100 = {3}\n". format(ResultDialog,x,y,(x*y)/100))
      elif save_cfg == OFF:
          pass
      elif save_cfg == AUTO:
          file(file_name="history.txt",file_mode="a",file_write="{0} ({1} * {2})/100 = {3}\n". format(ResultDialog,x,y,(x*y)/100))
      else:
          error_msg(save_err_msg,"","")

def Mod(x,y,ResultDialog,save_cfg,file_name,save_err_msg):
    print("{0} {1} % {2} = {3}". format(ResultDialog,x,y,x%y))

    if save_cfg == ON:
        file(file_name=file_name,file_mode="a",file_write="{0} {1} % {2} = {3}\n". format(ResultDialog,x,y,x%y))
    elif save_cfg == OFF:
        pass
    elif save_cfg == AUTO:
        file(file_name="history.txt",file_mode="a",file_write="{0} {1} % {2} = {3}\n". format(ResultDialog,x,y,x%y))
    else:
        error_msg(save_err_msg,"","")

def FullDivision(x,y,ResultDialog,save_cfg,file_name,save_err_msg):
    print("{0} {1} // {2} = {3}". format(ResultDialog,x,y,x//y))

    if save_cfg == ON:
        file(file_name=file_name,file_mode="a",file_write="{0} {1} // {2} = {3}\n". format(ResultDialog,x,y,x//y))
    elif save_cfg == OFF:
        pass
    elif save_cfg == AUTO:
        file(file_name="history.txt",file_mode="a",file_write="{0} {1} // {2} = {3}\n". format(ResultDialog,x,y,x//y))
    else:
        error_msg(save_err_msg,"","")

def TakingExponents(x,y,ResultDialog,save_cfg,file_name,save_err_msg):
    print("{0} {1} ** {2} = {3}". format(ResultDialog,x,y,x**y))

    if save_cfg == ON:
        file(file_name=file_name,file_mode="a",file_write="{0} {1} ** {2} = {3}\n". format(ResultDialog,x,y,x**y))
    elif save_cfg == OFF:
        pass
    elif save_cfg == AUTO:
        file(file_name="history.txt",file_mode="a",file_write="{0} {1} ** {2} = {3}\n". format(ResultDialog,x,y,x**y))
    else:
        error_msg(save_err_msg,"","")

def TakingRoots(x,y,ResultDialog,save_cfg,file_name,save_err_msg):
    print("{0} {1} / (1/{2}) = {3}". format(ResultDialog,x,y,x**(1/y)))

    if save_cfg == ON:
        file(file_name=file_name,file_mode="a",file_write="{0} {1} / (1/{2}) = {3}\n". format(ResultDialog,x,y,x**(1/y)))
    elif save_cfg == OFF:
        pass
    elif save_cfg == AUTO:
        file(file_name="history.txt",file_mode="a",file_write="{0} {1} / (1/{2}) = {3}\n". format(ResultDialog,x,y,x**(1/y)))
    else:
        error_msg(save_err_msg,"","")

def SqaureRoot(x,ResultDialog,save_cfg,file_name,save_err_msg):
    print("{0} {1} ** (1/2) = {2}". format(ResultDialog,x,x**(1/2)))

    if save_cfg == ON:
        file(file_name=file_name,file_mode="a",file_write="{0} {1} ** (1/2) {2} = {3}\n". format(ResultDialog,x,x**(1/2)))
    elif save_cfg == OFF:
        pass
    elif save_cfg == AUTO:
        file(file_name="history.txt",file_mode="a",file_write="{0} {1} ** (1/2) {2} = {3}\n". format(ResultDialog,x,x**(1/2)))
    else:
        error_msg(save_err_msg,"","")

def all_math_operations(optDialog,first_opt_dialog,second_opt_dialog,third_opt_dialog,fourth_opt_dialog,fifth_opt_dialog,sixth_opt_dialog,seventh_opt_dialog,eighth_opt_dialog,ninth_opt_dialog,tenth_opt_dialog,SelectOptDialog,nod,ntd,resdialog,divisionzerocheckdialog,errdg,addition_options_one,addition_options_two,addition_options_three,addition_options_four,addition_options_five,extraction_options_one,extraction_options_two,extraction_options_three,extraction_options_four,extraction_options_five,multiplication_options_one,multiplication_options_two,multiplication_options_three,multiplication_options_four,multiplication_options_five,division_options_one,division_options_two,division_options_three,division_options_four,division_options_five,percentage_options_one,percentage_options_two,percentage_options_three,percentage_options_four,percentage_options_five,fulldivision_options_one,fulldivision_options_two,fulldivision_options_three,fulldivision_options_four,fulldivision_options_five,takingexponents_options_one,takingexponents_options_two,takingexponents_options_three,takingexponents_options_four,takingexponents_options_five,takingroots_options_one,takingroots_options_two,takingroots_options_three,takingroots_options_four,takingroots_options_five,squareroot_options_one,squareroot_options_two,squareroot_options_three,squareroot_options_four,squareroot_options_five,mod_options_one,mod_options_two,mod_options_three,mod_options_four,mod_options_five):
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
    print(tenth_opt_dialog)
    select_func = str(input(SelectOptDialog))
    number_one=input(nod)
    number_two=input(ntd)
    if select_func == addition_options_one or select_func == addition_options_two or select_func == addition_options_three or select_func == addition_options_four or select_func == addition_options_five:
        Addition(number_one,number_two,resdialog,save_cfg=OFF,file_name="",save_err_msg="")
    elif select_func == extraction_options_one or select_func == extraction_options_two or select_func == extraction_options_three or select_func == extraction_options_four or select_func == extraction_options_five:
        Extraction(number_one,number_two,resdialog,save_cfg=OFF,file_name="",save_err_msg="")
    elif select_func == multiplication_options_one or select_func == multiplication_options_two or select_func == multiplication_options_three or select_func == multiplication_options_four or select_func == multiplication_options_five:
        Multiplication(number_one,number_two,resdialog,save_cfg=OFF,file_name="",save_err_msg="")
    elif select_func == division_options_one or select_func == division_options_two or select_func == division_options_three or select_func == division_options_four or select_func == division_options_five:
        Division(number_one,number_two,resdialog,divisionzerocheckdialog,save_cfg=OFF,file_name="",save_err_msg="")
    elif select_func == percentage_options_one or select_func == percentage_options_two or select_func == percentage_options_three or select_func == percentage_options_four or select_func == percentage_options_five:
        Percentage(number_one,number_two,resdialog,save_cfg=OFF,file_name="",save_err_msg="")
    elif select_func == fulldivision_options_one or select_func == fulldivision_options_two or select_func == fulldivision_options_three or select_func == fulldivision_options_four or select_func == fulldivision_options_five:
        FullDivision(number_one,number_two,resdialog,save_cfg=OFF,file_name="",save_err_msg="")
    elif select_func == takingexponents_options_one or select_func == takingexponents_options_two or select_func == takingexponents_options_three or select_func == takingexponents_options_four or select_func == takingexponents_options_five:
        TakingExponents(number_one,number_two,resdialog,save_cfg=OFF,file_name="",save_err_msg="")
    elif select_func == takingroots_options_one or select_func == takingroots_options_two or select_func == takingroots_options_three or select_func == takingroots_options_four or select_func == takingroots_options_five:
        TakingRoots(number_one,number_two,resdialog,save_cfg=OFF,file_name="",save_err_msg="")
    elif select_func == squareroot_options_one or select_func == squareroot_options_two or select_func == squareroot_options_three or select_func == squareroot_options_four or select_func == squareroot_options_five:
        SqaureRoot(number_one,resdialog,save_cfg=OFF,file_name="",save_err_msg="")
    elif select_func == mod_options_one or select_func == mod_options_two or select_func == mod_options_three or select_func == mod_options_four or select_func == mod_options_five:
        Mod(number_one,number_two,resdialog,save_cfg=OFF,file_name="",save_err_msg="")
    else:
        error_msg(errdg,"","")
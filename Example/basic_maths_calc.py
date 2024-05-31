#!/usr/bin/python3
""" Basic_Maths ile yapılmış bir örnek programdır. (Basic_Maths) kullanımına örnek olması amaçlı yazılmıştır.
"basic_maths_calc.py" adlı dosyanın paylaşılmasına (internette blog/gönderi vs.) gönderilerinde paylaşılmasına @LinuxUsersLinuxMint tarafından izin verilmiştir.
It is a example program made with Basic_Maths. It was written to serve as an example of (Basic_Maths) usage.
Sharing of the file named "basic_maths_calc.py" in posts (blog/post etc. on the internet) has been given permission by @LinuxUsersLinuxMint. """

from ..Basic_Maths.Basic_Maths import *

input_dialog = str("Enter the number: ")
error_dialog = str("Invalid process...")
resultdialog = str("Result:")

InputN1N2()

select=print('Select (Add, Ext, Mul, Div, Per, FullDiv, TakeEx): ')

input_select = str(input('Which process?'))
select_func = input_select


if select=="Add":
    Addition(number_one,number_two,resultdialog)
elif select=="Ext":
    Extraction(number_one,number_two,resultdialog)
elif select=="Mul":
    Multiplication(number_one,number_two,resultdialog)
elif select=="Div":
    Division(number_one,number_two,resultdialog,"The second number cannot be zero in division!")
elif select=="Per":
    Percentage(number_one,number_two,resultdialog)
elif select=="FullDiv":
    FullDivision(number_one,number_two,resultdialog)
elif select=="TakeEx":
    TakingExponents(number_one,number_two,resultdialog)
else:
    error_msg()
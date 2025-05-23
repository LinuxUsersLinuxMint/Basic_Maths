#!/usr/bin/python3
""" Basic_Maths ile yapılmış bir örnek programdır. (Basic_Maths) kullanımına örnek olması amaçlı yazılmıştır.
"test.py" adlı dosyanın paylaşılmasına (internette blog/gönderi vs.) gönderilerinde paylaşılmasına @LinuxUsersLinuxMint tarafından izin verilmiştir.
It is a example program made with Basic_Maths. It was written to serve as an example of (Basic_Maths) usage.
Sharing of the file named "test.py" in posts (blog/post etc. on the internet) has been given permission by @LinuxUsersLinuxMint. """

import Basic_Maths
from Basic_Maths.Lib.parameters import *

Basic_Maths.LibAbout()
Basic_Maths.all_math_operations("Select Operations: ","1. Addition","2. Extraction","3. Multiplication","4. Division","5. Percentage","6. FullDivision","7. TakingExponents","8. TakingRoots","9. SquareRoot","10. Mod","Select a transaction?: ","Enter the 1st number: ","Enter the 2nd number: ","Result:","Numbers cannot be zero in division!","Invalid Process!","1","add","addition","Addition","Toplama","2","ext","extraction","Extraction","Çıkarma","3","mul","multiplication","Multiplication","Çarpma","4","div","division","Division","Bölme","5","per","percentage","Percentage","Yüzdelik hesaplama","6","fulldiv","fulldivision","FullDivision","Tam bölüm","7","takingexp","takingexponents","TakingExponents","Üslü sayı alma","8","takingrt","takingroots","TakingRoots","Kök Alma","9","sqrt","squareroot","SquareRoot","Karekök","10","Mod","Modulus operation","","")

Basic_Maths.Addition(10,5,"RESULT:",save_cfg=ON,file_name="test.txt",save_err_msg="Error_msg")
Basic_Maths.Extraction(20,5,"RESULT:",save_cfg=ON,file_name="test.txt",save_err_msg="Error_msg")
Basic_Maths.Multiplication(30,5,"RESULT:",save_cfg=ON,file_name="test.txt",save_err_msg="Error_msg")
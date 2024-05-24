#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
Basic_Maths Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Basic_Maths All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/Basic_Maths
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/Basic_Maths"""

# Library functions

from lib_ver_info import *

def p(userString):
    print(userString)

def LibAbout():
    p("Python Library Name: {0}", format(PYTHON_LIB_NAME))
    p("Python Library Version: {0}\n", format(PYTHON_LIB_VER))
    p("Python Library Support OS: {0}\n", format(PYTHON_LIB_SUPPORT_PLATFORM))
    p("Python Library Licence Name: {0}\n", format(PYTHON_LIB_LICENCE))
    p("Python Library Author Name: {0}\n", format(PYTHON_LIB_AUTHOR))
    p("Python Library Release Date: {0}\n", format(PYTHON_LIB_RELEASE_DATE))

# TR (Türkçe):
# NOT: "Kütüphane fonksiyonları" başlığı altındaki fonksiyonlar kullanımı isteğe bağlıdır ancak "Basic_Maths" kütüphanesini kullanan bir "Python" yazılımında kullanıcıya kullanılan kütüphane hakkında bilgi vermek amacıyla kullanılabilir.

# EN (English):
# NOTE: The functions under the "Library functions" heading are optional, but can be used in a "Python" software that uses the "Basic_Maths" library to provide information to the user about the library used.

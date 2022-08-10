import os,platform;from time import sleep

riki=platform.architecture()[0]

os.system('git pull')

if riki=="32bit":
    print('Sorry Brother Update Your Phone..\.')

elif riki=="64bit":
    os.system('am start https://www.facebook.com/Itz.D3M09')
    __import__("D3M0")._Stanford_()

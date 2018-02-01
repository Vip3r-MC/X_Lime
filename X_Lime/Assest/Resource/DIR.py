# -*- coding: utf-8 -*-
import os
from termcolor import colored

dir_path = os.path.dirname(os.path.realpath(__file__))
c_dir_path = colored(dir_path, 'red', attrs=['bold'])
apk_directory = colored('Move the apk file to this dircetory and Enter the name of the apk', 'green', attrs=['bold'])
alone = colored('(alone)', 'red', attrs=['bold']) 
apk_enter = colored('Enter the name of the apk ⬎', 'green', attrs=['bold'])
choose_directory = colored('Enter the apk dircetory ⬎', 'green', attrs=['bold'])    
exampe = colored('/root/Desktop/myapk.apk', 'red', attrs=['bold'])  
clear = lambda: os.system('cls')
eg = colored('eg:(', 'green', attrs=['bold'])
eg_2 = colored(')', 'green', attrs=['bold'])
back = colored('Go Back', 'blue', attrs=['bold'])
b1_sign = colored('(', 'red', attrs=['bold'])
name_1 = colored('Enter the name for the rc file', 'green', attrs=['bold'])
NO = colored('No', 'red', attrs=['bold'])
YES = colored('Yes', 'green', attrs=['bold'])
b2_sign = colored(')', 'red', attrs=['bold'])

x1 = '\033[1;32m1\033[1;m'#1
x2 = '\033[1;32m2\033[1;m'#2
x3 = '\033[1;32m3\033[1;m'#3
x4 = '\033[1;32m4\033[1;m'#4
x5 = '\033[1;32m5\033[1;m'#5
x6 = '\033[1;32m6\033[1;m'#6
x0 = '\033[1;32m0\033[1;m'#0
a1_sign = '\033[1;37m[\033[1;m'
a2_sign = '\033[1;37m]\033[1;m'
d_sign = '\033[1;37m[\033[1;m''\033[1;32m--\033[1;m''\033[1;37m]\033[1;m'
d1_sign = '\033[1;37m[\033[1;m''\033[1;32m-\033[1;m''\033[1;37m]\033[1;m'
d_sign1 = '\033[1;37m: \033[1;m'
d_sign2 = '\033[1;37m[\033[1;m''\033[1;31mXX\033[1;m''\033[1;37m]\033[1;m'

def c_print(s):
    os_size = int(subprocess.check_output(['stty', 'size']).split()[1])
pass

def space():
    print("")
pass

def payload1():
    print '\033[1;38m(1)android/meterpreter/reverse_tcp\033[1;m'
    print '\033[1;38m(2)android/meterpreter/reverse_http\033[1;m'
    print '\033[1;38m(3)android/meterpreter/reverse_https\033[1;m'
pass

def cls():
	os.system('cls' if os.name=='nt' else 'clear')
pass

def del_cls():
	os.system('find Assest -name *.pyc -delete')
pass
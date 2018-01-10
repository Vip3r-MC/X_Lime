#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
import shutil
import sys
import time
import progressbar

from termcolor import colored
from termcolor import cprint
from colorama import init
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty())
#Symbols 
x1 = '\033[1;32m1\033[1;m'
x2 = '\033[1;32m2\033[1;m'
x3 = '\033[1;32m3\033[1;m'
x4 = '\033[1;32m4\033[1;m'
x5 = '\033[1;32m5\033[1;m'
x6 = '\033[1;32m6\033[1;m'
a1_sign = '\033[1;37m[\033[1;m'
a2_sign = '\033[1;37m]\033[1;m'
d_sign = '\033[1;37m[\033[1;m''\033[1;32m--\033[1;m''\033[1;37m]\033[1;m'
d_sign1 = '\033[1;37m: \033[1;m'
d_sign2 = '\033[1;37m[\033[1;m''\033[1;31mXX\033[1;m''\033[1;37m]\033[1;m'

#Choice 1 apk
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


def cls():
	os.system('cls' if os.name=='nt' else 'clear')
pass

def hacking():
    print colored('            ======================================================            ', 'green', attrs=['bold'])	
    print colored('            ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗             ', 'red', attrs=['bold'])
    print colored('            ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝             ', 'red', attrs=['bold'])
    print colored('            ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗            ', 'red', attrs=['bold'])
    print colored('            ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║            ', 'red', attrs=['bold'])
    print colored('            ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝            ', 'red', attrs=['bold'])
    print colored('            ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝             ', 'red', attrs=['bold'])
    print colored('            ======================================================            ', 'green', attrs=['bold'])
pass

cls()
hacking()

def c_print(s):
	os_size = int(subprocess.check_output(['stty', 'size']).split()[1])
pass

def space():
	print("")
pass

cls()
def derp():
    print("          ─────────▄▄───────────────────▄▄──")
    print("          ──────────▀█───────────────────▀█─")
    print("          ──────────▄█───────────────────▄█─")
    print("          ──█████████▀───────────█████████▀─")
    print("          ───▄██████▄─────────────▄██████▄──")
    print("          ─▄██▀────▀██▄─────────▄██▀────▀██▄")
    print("          ─██────────██─────────██────────██")
    print("          ─██───██───██─────────██───██───██")
    print("          ─██────────██─────────██────────██")
    print("          ──██▄────▄██───────────██▄────▄██─")
    print("          ───▀██████▀─────────────▀██████▀──")
    print("          ──────────────────────────────────")
    print("          ──────────────────────────────────")
    print("          ──────────────────────────────────")
    print("          ───────────█████████████──────────")
    print("          ──────────────────────────────────")
    print("          ──────────────────────────────────")
pass
def X():
    print("    ....▓▓▓▓")
    print("    ..▓▓......▓")
    print("    ..▓▓......▓▓..................▓▓▓▓")
    print("    ..▓▓......▓▓..............▓▓......▓▓▓▓")
    print("    ..▓▓....▓▓..............▓......▓▓......▓▓")
    print("    ....▓▓....▓............▓....▓▓....▓▓▓....▓▓")
    print("    ......▓▓....▓........▓....▓▓..........▓▓....▓")
    print("    ........▓▓..▓▓....▓▓..▓▓................▓▓")
    print("    ........▓▓......▓▓....▓▓")
    print("    .......▓......................▓")
    print("    .....▓.........................▓")
    print("    ....▓......^..........^......▓")
    print("    ....▓............❤............▓")
    print("    ....▓..........................▓")
    print("    ......▓..........ٮ..........▓")
    print("    ..........▓▓..........▓▓")
pass
def terminal_resize1():
    subprocess.call(['/usr/bin/resize', '-s', '18', '48'])
pass
def terminal_resize2():
    subprocess.call(['/usr/bin/resize', '-s', '9', '78'])
pass

def terminal_resize3():
    subprocess.call(['/usr/bin/resize', '-s', '23', '53'])
pass

def terminal_resize4():
    subprocess.call(['/usr/bin/resize', '-s', '20', '51'])
pass

def start_textart():
    print colored('================================================', 'red', attrs=['bold'])
    print colored(' ##:::: ##: ##::::::: ####: ##:::: ##: ########:', 'green', attrs=['bold'])
    print colored('. ##:: ##:: ##:::::::. ##:: ###:: ###: ##.....::', 'green', attrs=['bold'])
    print colored(':. ## ##::: ##:::::::: ##:: #### ####: ##:::::::', 'green', attrs=['bold'])
    print colored('::. ###:::: ##:::::::: ##:: ## ### ##: ######:::', 'green', attrs=['bold'])
    print colored(':: ## ##::: ##:::::::: ##:: ##. #: ##: ##...::::', 'green', attrs=['bold'])
    print colored(': ##:. ##:: ##:::::::: ##:: ##:.:: ##: ##:::::::', 'green', attrs=['bold'])
    print colored(' ##:::. ##: ########: ####: ##:::: ##: ########:', 'green', attrs=['bold'])
    print colored('..:::::..::........::....::..:::::..::........::', 'green', attrs=['bold'])
    print colored('====================', 'red', attrs=['bold']), colored('X_LIME', 'blue', attrs=['bold']), colored('====================', 'red', attrs=['bold'])
    print (d_sign + '\033[1;33mSELECT AN OPTION TO BEGIN: \033[1;m')
    print (a1_sign + x1 + a2_sign + '\033[1;32m Decomplie apk\033[1;m')
    print (a1_sign + x2 + a2_sign + '\033[1;32m Apk-2-Jar\033[1;m')
    print (a1_sign + x3 + a2_sign + '\033[1;32m Help\033[1;m')
    print (a1_sign + x4 + a2_sign + '\033[1;32m Help\033[1;m')
    print (a1_sign + x5 + a2_sign + '\033[1;32m Help\033[1;m')
    print (a1_sign + x6 + a2_sign + '\033[1;32m Help\033[1;m')
    pass
pass

def Loading():
	with progressbar.ProgressBar(max_value=30) as bar:
		for i in range(30):
			time.sleep(0.1)
			bar.update(i)
		pass
	pass
pass

def terminal_launch():
    os.system('gnome-terminal --hide-menubar')
pass

cls()
terminal_resize2()
hacking()
Loading()   
cls()
terminal_resize1()
start_textart()

choice_1 = raw_input(d_sign1)
terminal_resize3()
cls()
while choice_1 == '1':
	print colored('▂▂▃▃▄▄▅▅▆▆▇▇██▓▓▒▒░░APK DECOMPILE░░▒▒▓▓██▇▇▆▆▅▅▄▄▃▃▂▂', 'red', attrs=['bold'])
	space()
	derp()
	print('                        ' + d_sign + 'OPTIONS' + d_sign)
	#print(d_sign + apk_directory + alone)
	print(d_sign + choose_directory)
        print(d_sign + eg + exampe + eg_2)
	apk_file = raw_input(d_sign1)
	if apk_file.endswith('.apk'):
            os.system('apktool d '+apk_file)
        else:
            print (d_sign2), colored('Wrong file format!!!!', 'red', attrs=['reverse', 'bold'])
pass

cls()
while choice_1 =='2':
    terminal_resize4()
    print colored('▂▂▃▃▄▄▅▅▆▆▇▇██▓▓▒▒░░!APK-2-JAR!░░▒▒▓▓██▇▇▆▆▅▅▄▄▃▃▂▂', 'red', attrs=['bold'])
    X()
    print(d_sign + choose_directory)    
    print(d_sign + eg + exampe + eg_2)
    apk_file = raw_input(d_sign1)
    os.system('d2j-dex2jar ' + apk_file)
    pass

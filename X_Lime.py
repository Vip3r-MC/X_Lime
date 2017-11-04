#!/usr/bin/python
from termcolor import colored
import os

x1 = '\033[1;32m1\033[1;m'
x2 = '\033[1;32m2\033[1;m'
x3 = '\033[1;32m3\033[1;m'
x4 = '\033[1;32m4\033[1;m'
x5 = '\033[1;32m5\033[1;m'
x6 = '\033[1;32m6\033[1;m'
a1_sign = '\033[1;37m[\033[1;m'
a2_sign = '\033[1;37m]\033[1;m'
d_sign = '\033[1;37m[\033[1;m''\033[1;32m--\033[1;m''\033[1;37m]\033[1;m'
dir_path = os.path.dirname(os.path.realpath(__file__))
c_dir_path = colored(dir_path, 'red', attrs=['bold'])


def cls():
	os.system('cls' if os.name=='nt' else 'clear')
	pass

clear = lambda: os.system('cls')
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
print (a1_sign + x2 + a2_sign + '\033[1;32m Inject Apk\033[1;m')
print (a1_sign + x3 + a2_sign + '\033[1;32m Help\033[1;m')
print (a1_sign + x4 + a2_sign + '\033[1;32m Help\033[1;m')
print (a1_sign + x5 + a2_sign + '\033[1;32m Help\033[1;m')
print (a1_sign + x6 + a2_sign + '\033[1;32m Help\033[1;m')


choice_1 = raw_input('\033[1;37m: \033[1;m')

if choice_1 == '1':
	cls()
	print(d_sign + 'move the apk file to this dircetory ' + c_dir_path)
elif choice_1 == '2':
	cls()
	print '2'
elif choice_1 == '3':
	cls()
	print '3'
elif choice_1 == '4':
	cls()
	print '4'
elif choice_1 == '5':
	cls()
	print '5'
elif choice_1 == '6':
	cls()
	print '6'
	pass

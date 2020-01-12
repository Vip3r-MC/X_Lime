#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import apt
from termcolor import colored

cache = apt.Cache()
not_installed = []

print colored("*----Checking for Missing Packages----*", 'green', attrs=['bold'])

if cache['apktool'].is_installed:
	print colored("apktool:", 'red', attrs=['bold']), colored("...............[ located ]" , 'green', attrs=['bold'])
else:
	not_installed.append('apktool')
	print colored("apktool:", 'red', attrs=['bold']), colored("...............[ not present ]" , 'red', attrs=['bold'])
if cache['zipalign'].is_installed:
	print colored("zipalign:", 'red', attrs=['bold']), colored("..............[ located ]", 'green', attrs=['bold'])
else:
	not_installed.append('zipalign')
	print colored("zipalign:", 'red', attrs=['bold']), colored("...............[ not present ]" , 'red', attrs=['bold'])
if cache['python-termcolor'].is_installed:
	print colored("python-termcolor:", 'red', attrs=['bold']), colored("......[ located ]", 'green', attrs=['bold'])
else:
	not_installed.append('python-termcolor')
	print colored("python-termcolor:", 'red', attrs=['bold']), colored("...............[ not present ]" , 'red', attrs=['bold'])
if cache['dex2jar'].is_installed:
	print colored("dex2jar:", 'red', attrs=['bold']), colored("...............[ located ]", 'green', attrs=['bold'])
else:
	not_installed.append('dex2jar')
	print colored("dex2jar:", 'red', attrs=['bold']), colored("...............[ not present ]" , 'red', attrs=['bold'])

if not_installed:
	print colored("*----Installing Missing Package----*", 'green', attrs=['bold'])
else:
	pass
if 'apktool' in not_installed:
	os.system("xterm -fn 6x10 -geometry 86x23-0+0 -e 'sudo apt-get install apktool -y'")
	print colored("apktool:", 'red', attrs=['bold']), colored("...............[ installed ]", 'green', attrs=['bold'])
if 'zipalign' in not_installed:
	os.system("xterm -fn 6x10 -geometry 86x23-0+0 -e 'sudo apt-get install zipalign -y'")
	print colored("zipalign:", 'red', attrs=['bold']), colored("...............[ installed ]", 'green', attrs=['bold'])
if 'python-termcolor' in not_installed:
	os.system("xterm -fn 6x10 -geometry 86x23-0+0 -e 'sudo apt-get install python-termcolor -y'")
	print colored("python-termcolor:", 'red', attrs=['bold']), colored("...............[ installed ]", 'green', attrs=['bold'])
if 'dex2jar' in not_installed:
	os.system("xterm -fn 6x10 -geometry 86x23-0+0 -e 'sudo apt-get install dex2jar -y'")
	print colored("dex2jar:", 'red', attrs=['bold']), colored("...............[ installed ]", 'green', attrs=['bold'])

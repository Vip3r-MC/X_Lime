#!/usr/bin/python2
# -*- coding: utf-8 -*-w
import os
import signal

os.system("gnome-terminal --geometry=+535+250 --hide-menubar -e 'bash -c \"sudo python2 Assest/run.py; exec bash\"'")
os.kill(os.getppid(), signal.SIGHUP)
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import signal

os.system("gnome-terminal --hide-menubar -e 'bash -c \"python Assest/xlime_run.py; exec bash\"'")
os.kill(os.getppid(), signal.SIGHUP)
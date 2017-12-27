import os
import signal

os.system("gnome-terminal --hide-menubar -e 'bash -c \"./xlime_run.py; exec bash\"'")
os.kill(os.getppid(), signal.SIGHUP)
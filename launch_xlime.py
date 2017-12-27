import os
import signal

os.system("gnome-terminal --hide-menubar -e 'bash -c \"./X_Lime.py; exec bash\"'")
os.kill(os.getppid(), signal.SIGHUP)
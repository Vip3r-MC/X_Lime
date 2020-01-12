import sys
import os
rows, columns = os.popen('stty size', 'r').read().split()

def terminal_default():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=rows, cols=columns))
pass   

def terminal_resize1():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=17, cols=48))
pass
def terminal_resize2():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=9, cols=78))
pass
def terminal_resize3():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=23, cols=53))
pass
def terminal_resize4():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=21, cols=51))
pass
def terminal_resize5():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=14, cols=34))
    pass
def terminal_resize6():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=27, cols=93))
    pass
def terminal_resize7():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=18, cols=49))
    pass
def terminal_resize8():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=14, cols=38))
    pass
def terminal_resize9():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=20, cols=30))
    pass
def terminal_resize10():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=20, cols=53))
    pass
def terminal_return():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=24, cols=80))
    pass
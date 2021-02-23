import time
import serial
import mpv
import tkinter as tk
from tkinter import filedialog

# TK - for file select
root = tk.Tk()
root.withdraw()

# Path for selecting single file
#path = filedialog.askopenfilename()

# Path for selecting directory
path = filedialog.askdirectory()

#MPV
player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True)
player.play(path)

# BT Serial



while True:
    try:
        s = serial.Serial('/dev/rfcomm0', 9600)
        print('Connected to serial')
        break
    except:
        print('Cound not connect to serial, trying again in 5 sec')
        x = range(5, 0, -1)
        for i in x:
            print(i, '..')
            time.sleep(1)

msg = ''

def recieve():

    global msg

    byte = s.read()
    strIn = byte.decode("utf-8")

    if strIn == '>':
        return msg
        msg = ''
    elif strIn == '<':
        msg = ''
    else:
        msg += strIn


while True:

    
    cmd = recieve()

    print(cmd)

    if cmd == 'state' or cmd == 'play' or cmd == 'pause'  :
        print('changing play state')
        if player._get_property('pause'):
            player._set_property('pause', False)
        else:
            player._set_property('pause', True)
    elif cmd == 'forward10':
        player.command('seek', 10, 'relative')
    elif cmd == 'back10':
        player.command('seek', -10, 'relative')
    elif cmd == 'prev':
        print('Prev in playlist')
        player.playlist_prev();
    elif cmd == 'next':
        print('Next in playlist')
        player.playlist_next()

    


import serial
import mpv

#MPV
player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True)
player.play('/home/carter/media/video/regularShow/The Regular Show S01-S08 + Movie + Shorts [1080p BluRay x265 HEVC 10bit]/Season 1/')

# BT Serial
s = serial.Serial('/dev/rfcomm0', 9600)
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

    

    if cmd == 'state' or cmd == 'play' or cmd == 'pause'  :
        print('changing play state')
        if player._get_property('pause'):
            player._set_property('pause', False)
        else:
            player._set_property('pause', True)
    elif cmd == 'forward':
        player.command('seek', 10, 'relative')
    elif cmd == 'back':
        player.command('seek', -10, 'relative')
    elif cmd == 'prev':
        print('Prev in playlist')
        player.playlist_prev();
    elif cmd == 'next':
        print('Next in playlist')
        player.playlist_next()

    


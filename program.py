# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_apds9960.apds9960 import APDS9960
import qwiic_joystick 
import os
import simpleaudio as sa
from pydub import AudioSegment

i2c = board.I2C()
apds = APDS9960(i2c)
myJoystick = qwiic_joystick.QwiicJoystick()
myJoystick.begin()

apds.enable_proximity = True

c = False
d = False
e = False
f = False
g = False
a = False
b = False

csound = 'audios/csound40.wav'
dsound = 'audios/dsound.wav'
esound = 'audios/esound.wav'
fsound = 'audios/fsound.wav'
gsound = 'audios/gsound.wav'
asound = 'audios/asound.wav'
bsound = 'audios/bsound.wav'



while True:
    if apds.proximity > 250:
        c = True
    if myJoystick.horizontal == 0:
        if c:
            print("yah!")
            wave_obj = sa.WaveObject.from_wave_file(csound)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            print("done")
    print(c)
    time.sleep(0.2)

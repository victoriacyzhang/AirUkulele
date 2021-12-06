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

singles = ['audios/singles/c_single_40.wav', 'audios/singles/csharp_single_40.wav', 'audios/singles/d_single_40.wav', 'audios/singles/dsharp_single_40.wav', 'audios/singles/e_single_40.wav', 'audios/singles/f_single_40.wav', 'audios/singles/fsharp_single_40.wav', 'audios/singles/g_single_40.wav', 'audios/singles/gsharp_single_40.wav', 'audios/singles/a_single_40.wav', 'audios/singles/asharp_single_40.wav', 'audios/singles/b_single_40.wav', 'audios/singles/c5_single_40.wav']

dividend = 255 / (len(singles) - 1)
while True:
    currp = apds.proximity
    index = int(currp // dividend)
    if (index == 10) and ((currp % dividend) > 0):
        index = index + 1
    currSingleName = singles[index]
    if myJoystick.horizontal == 0:
        wave_obj = sa.WaveObject.from_wave_file(currSingleName)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    #time.sleep(0.2)

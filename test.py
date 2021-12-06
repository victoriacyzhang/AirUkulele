import qwiic
import time
import qwiic_joystick
import os
import simpleaudio as sa
from pydub import AudioSegment

joystick = qwiic_joystick.QwiicJoystick()
joystick.begin()
ToF = qwiic.QwiicVL53L1X()

singles = ['audios/singles/c_single_40.wav', 'audios/singles/csharp_single_40.wav', 'audios/singles/d_single_40.wav', 'audios/singles/dsharp_single_40.wav', 'audios/singles/e_single_40.wav', 'audios/singles/f_single_40.wav', 'audios/singles/fsharp_single_40.wav', 'audios/singles/g_single_40.wav', 'audios/singles/gsharp_single_40.wav', 'audios/singles/a_single_40.wav', 'audios/singles/asharp_single_40.wav', 'audios/singles/b_single_40.wav', 'audios/singles/c5_single_40.wav']

distanceRange = [30, 280]
dividend = 250 / (len(singles) - 1)
while True:
    try:
        ToF.start_ranging()
        time.sleep(.005)
        distance = ToF.get_distance()
        time.sleep(.005)
        ToF.stop_ranging()
        if distance < distanceRange[0]:
            distance = distanceRange[0]
        elif distance > distanceRange[1]:
            distance = distanceRange[1]
        distance -= 30
        index = int(distance // dividend)
        if (index == 11) and ((distance % dividend) > 0):
            index = index + 1
        currSingleName = singles[index]
        if joystick.horizontal == 0:
            wave_obj = sa.WaveObject.from_wave_file(currSingleName)
            play_obj = wave_obj.play()
            play_obj.wait_done()
        print(distance)
    except Exception as e:
        print(e)

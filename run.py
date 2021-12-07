import qwiic
import time
import qwiic_joystick
import os
import simpleaudio as sa
from pydub import AudioSegment
import busio
import board
from adafruit_bus_device.i2c_device import I2CDevice
from struct import pack, unpack

DEVICE_ADDRESS = 0x6f  # device address of our button
STATUS = 0x03 # reguster for button status
AVAILIBLE = 0x1
BEEN_CLICKED = 0x2
IS_PRESSED = 0x4

# The follow is for I2C communications
i2c = busio.I2C(board.SCL, board.SDA)
device = I2CDevice(i2c, DEVICE_ADDRESS)

def write_register(dev, register, value, n_bytes=1):
    # Write a wregister number and value
    buf = bytearray(1 + n_bytes)
    buf[0] = register
    buf[1:] = value.to_bytes(n_bytes, 'little')
    with dev:
        dev.write(buf)

def read_register(dev, register, n_bytes=1):
    # write a register number then read back the value
    reg = register.to_bytes(1, 'little')
    buf = bytearray(n_bytes)
    with dev:
        dev.write_then_readinto(reg, buf)
    return int.from_bytes(buf, 'little')

# clear out LED lighting settings. For more info https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/8/Qwiic_Button_I2C_Register_Map.pdf
write_register(device, 0x1A, 1)
write_register(device, 0x1B, 0, 2)
write_register(device, 0x19, 0)

joystick = qwiic_joystick.QwiicJoystick()
joystick.begin()
ToF = qwiic.QwiicVL53L1X()

singles = ['audios/singles/c_single_40.wav', 'audios/singles/csharp_single_40.wav', 'audios/singles/d_single_40.wav', 'audios/singles/dsharp_single_40.wav', 'audios/singles/e_single_40.wav', 'audios/singles/f_single_40.wav', 'audios/singles/fsharp_single_40.wav', 'audios/singles/g_single_40.wav', 'audios/singles/gsharp_single_40.wav', 'audios/singles/a_single_40.wav', 'audios/singles/asharp_single_40.wav', 'audios/singles/b_single_40.wav', 'audios/singles/c5_single_40.wav']

majors = ['audios/majorchords/cmajor_40.wav', 'audios/majorchords/csharpmajor_40.wav', 'audios/majorchords/dmajor_40.wav', 'audios/majorchords/dsharpmajor_40.wav', 'audios/majorchords/emajor_40.wav', 'audios/majorchords/fmajor_40.wav', 'audios/majorchords/fsharpmajor_40.wav', 'audios/majorchords/gmajor_40.wav', 'audios/majorchords/gsharpmajor_40.wav', 'audios/majorchords/amajor_40.wav', 'audios/majorchords/asharpmajor_40.wav', 'audios/majorchords/bmajor_40.wav', 'audios/majorchords/c5major_40.wav']

distanceRange = [30, 180]
dividend = 150 / (len(singles) - 1)

currButton = False
while True:
    try:
        btn_status = read_register(device, STATUS)
        # if pressed light LED
        if (btn_status&IS_PRESSED) !=0:
            if currButton == False:
                currButton = True
                write_register(device, 0x19, 255)
            elif currButton == True:
                currButton = False
                write_register(device, 0x19, 0)

        ToF.start_ranging()
        time.sleep(.005)
        distanceO = ToF.get_distance()
        time.sleep(.005)
        ToF.stop_ranging()
        if distanceO < distanceRange[0]:
            distance = distanceRange[0]
        elif distanceO > distanceRange[1]:
            distance = distanceRange[1]
        else:
            distance = distanceO
        distance -= 30
        index = int(distance // dividend)
        if (index == 11) and ((distance % dividend) > 0):
            index = index + 1
        currSingleName = singles[index]
        currMajorName = majors[index]
        if (joystick.horizontal < 3) or (joystick.horizontal > 1022):
            if currButton:
                wave_obj = sa.WaveObject.from_wave_file(currMajorName)
            else:
                wave_obj = sa.WaveObject.from_wave_file(currSingleName)
            play_obj = wave_obj.play()
            play_obj.wait_done()
        #print()
    except Exception as e:
        print(e)

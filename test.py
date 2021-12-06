import qwiic
import time

ToF = qwiic.QwiicVL53L1X()
while True:
    try:
        ToF.start_ranging()
        time.sleep(.005)
        distance = ToF.get_distance()
        time.sleep(.005)
        ToF.stop_ranging()
        print(distance)
    except Exception as e:
        print(e)

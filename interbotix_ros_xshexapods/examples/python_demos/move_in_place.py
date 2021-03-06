import math
import time
from interbotix_xs_modules.hexapod import InterbotixHexapodXS

# This script makes the hexapod body rotate in place for approximately 20 seconds
#
# To get started, open a terminal and type 'roslaunch interbotix_xshexapod_control xshexapod_control.launch robot_model:=wxmark4'
# Then change to this directory and type 'python rotate_in_place.py'

def main():

    bot = InterbotixHexapodXS('cavex')
    #bot.hex.move_in_place(z=0.18) #0.1 was a bit too low
    bot.hex.modify_stance(-0.015)

    # translate in X
    for step in range(51):
        x = 0.05 * math.sin(2*math.pi * step/50.0)
        bot.hex.move_in_place(x=x, moving_time=0.15, blocking=False)
        time.sleep(0.04)
    time.sleep(0.2)

    # translate in Y
    for step in range(51):
        y = 0.05 * math.sin(2*math.pi * step/50.0)
        bot.hex.move_in_place(y=y, moving_time=0.15, blocking=False)
        time.sleep(0.04)
    time.sleep(0.2)

    # translate in Z
    for step in range(51):
        z = 0.19 + 0.05 * math.sin(2*math.pi * step/50.0)		#0.1 was a bit too low (first term)
        bot.hex.move_in_place(z=z, moving_time=0.15, blocking=False)
        time.sleep(0.04)
    time.sleep(0.2)

    # roll around X
    for step in range(51):
        roll = 0.3 * math.sin(2*math.pi * step/50.0)
        bot.hex.move_in_place(roll=roll, moving_time=0.15, blocking=False)
        time.sleep(0.04)
    time.sleep(0.2)

    # pitch around Y
    for step in range(51):
        pitch = 0.3 * math.sin(2*math.pi * step/50.0)
        bot.hex.move_in_place(pitch=pitch, moving_time=0.15, blocking=False)
        time.sleep(0.04)
    time.sleep(0.2)

    # yaw around Z
    for step in range(51):
        yaw = 0.3 * math.sin(2*math.pi * step/50.0)
        bot.hex.move_in_place(yaw=yaw, moving_time=0.15, blocking=False)
        time.sleep(0.04)
    time.sleep(0.2)
    

    #time.sleep(1)
    #bot.hex.move_in_place(z=0.06, moving_time=2.0, blocking=True) #so it doesn't "clunk" onto the ground
    #time.sleep(1)
    #bot.hex.move_in_place(z=0.03, moving_time=2.0, blocking=True)   
    #time.sleep(1)

    #bot.hex.reset_hexapod('sleep')

if __name__=='__main__':
    main()

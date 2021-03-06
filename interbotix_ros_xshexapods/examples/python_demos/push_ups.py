import math
import time
from interbotix_xs_modules.hexapod import InterbotixHexapodXS

# This script makes the hexapod body move up and down for approximately 20 seconds
#
# To get started, open a terminal and type 'roslaunch interbotix_xshexapod_control xshexapod_control.launch robot_model:=pxmark4'
# Then change to this directory and type 'python push_ups.py'

def main():
    bot = InterbotixHexapodXS('cavex')
    bot.hex.move_in_place(z=0.1)				#changed from 0.08 which was too low
    for step in range(500):
        z = 0.1 + 0.05 * math.sin(math.pi * step/25.0)#first term changed from 0.08 which was too low
        bot.hex.move_in_place(z=z, moving_time=0.15, blocking=False)
        time.sleep(0.04)
    bot.hex.reset_hexapod('home')

if __name__=='__main__':
    main()

from interbotix_xs_modules.hexapod import InterbotixHexapodXS

# This script makes the hexapod follow a straight trajectory
#
# To get started, open a terminal and type 'roslaunch interbotix_xshexapod_control xshexapod_control.launch robot_model:=mark4'
# Then change to this directory and type 'python walk_in_square.py'

height_stance = 0.15

def main():

    bot = InterbotixHexapodXS('cavex')

    bot.hex.move_in_place(z=height_stance)			#from 0.1

    # ...assuming the new height looks good, set it to be the new Home Pose height
    bot.hex.set_home_height(height_stance)

    bot.hex.modify_stance(-0.1)	#bot.hex.modify_stance(-0.02)

    #bot.hex.move_in_world(x_stride=0.1, num_cycles=5, gait_type="tripod")	
    # bot.hex.move_in_world(x_stride=0.1, num_cycles=5, gait_type="tripod", max_foot_height=0.12)
    bot.hex.move_in_world(x_stride=0.1, num_cycles=500, gait_type="tripod", max_foot_height=0.1)
    # bot.hex.move_in_world(x_stride=0.1, num_cycles=5, gait_type="tripod", max_foot_height=0.1,  mp=0.3) # 'times' mp and ap are confusing! Do not understand them.

    bot.hex.reset_hexapod("home")

if __name__=='__main__':
    main()

import itertools
import time
import numpy
import scipy
import matplotlib
import pypot.dynamixel
from inverse_kinematics import * 

if __name__ == '__main__':

    # we first open the Dynamixel serial port
    with pypot.dynamixel.DxlIO('/dev/tty.usbserial-AH00RA8U', baudrate=1000000) as dxl_io:
        print "Scan des ids"
        
        # we can scan the motors
        found_ids = [41,42,43]  # this may take several seconds
        print 'Detected:', found_ids

        # we power on the motors
        dxl_io.enable_torque(found_ids)

        # we get the current positions
        print 'Current pos:', dxl_io.get_present_position(found_ids)
        
        pos = leg_ik(170,-45, 35)
        
        positions = [   [170, -45, 35],
                        [170, -45, 0],
                        [170, -45, 35],
                        [170, 0, 35],
                        [170, 0, 0],
                        [170, 0, 35],
                        [170, 45, 35],
                        [170, 45, 0],
                        [170, 45, 35]]
        
        for position in positions:
            dxl_io.set_goal_position(dict(zip(found_ids, leg_ik(position[0], position[1], position[2]))))
            time.sleep(1)
            print dict(zip(found_ids, leg_ik(position[0], position[1], position[2])))
        
        # we get the current positions
        print 'New pos:', dxl_io.get_present_position(found_ids)
        
        # we power off the motors
        dxl_io.disable_torque(found_ids)
        time.sleep(1)  # we wait for 1s

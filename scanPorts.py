import itertools
import time
import numpy
import pypot.dynamixel

def moveMotor(dxl, motorId, angle):
    print "Move", motorId, "at",  angle
    dxl_io.set_goal_position({motorId: angle})
    time.sleep(0.2)
if __name__ == '__main__':

    # we first open the Dynamixel serial port
    with pypot.dynamixel.DxlIO('/dev/ttyUSB0', baudrate=1000000) as dxl_io:
        found_ids = [11,12,13, 
                     21,22,23, 
                     31,32,33, 
                     41,42,43, 
                     51,52,53, 
                     61,62,63
                    ]
        
        print 'Detected:', found_ids
        print(dxl_io.get_present_position(found_ids))
        for a in [0]:
            for i in found_ids:
                moveMotor(dxl_io, i, a)
        #for a in [-50]:
        #    for i in [12,32,52]:
        #        moveMotor(dxl_io, i, a)
        #moveMotor(dxl_io, 31, 30)

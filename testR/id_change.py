import itertools
import pypot.dynamixel

if __name__ == '__main__':

    with pypot.dynamixel.DxlIO('/dev/ttyUSB0', baudrate=1000000) as dxl_io:
          # we can scan the motors
        found_ids =  dxl_io.scan()  # this may take several seconds
        print 'Detected:', found_ids

        #new_old = [{10 : found_ids[0]}(10 , found_ids[0]),(11 , found_ids[1]), (12 , found_ids[2]) ]

        dxl_io.change_id({ found_ids[0] : 10})
        dxl_io.change_id({ found_ids[1] : 11})
        dxl_io.change_id({ found_ids[2] : 12})
        
        # we can scan the motors
        found_ids =  dxl_io.scan()  # this may take several seconds
        print 'Detected:', found_ids

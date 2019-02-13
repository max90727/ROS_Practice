#!/usr/bin/env python
import sys
import os
import rospy
from my_robot_msgs.srv import ComputeDiskArea, ComputeDiskAreaRequest

def compute_disk_area_client(radius):
    rospy.wait_for_service("ComputeDiskArea")
    try:
        compute_disk_area = rospy.ServiceProxy("ComputeDiskArea", ComputeDiskArea)
        resp = compute_disk_area.call(ComputeDiskAreaRequest(radius))
        return resp.area
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    argv = rospy.myargv()
    if len(argv) == 1:
        import random
        radius = random.randfloat(0, 100)
    elif len(argv) == 2:
        radius = float(argv[1])

    print("The area of the %f is %f" % (radius, compute_disk_area_client(radius)))

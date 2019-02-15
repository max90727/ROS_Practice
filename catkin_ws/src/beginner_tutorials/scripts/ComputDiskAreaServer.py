#!/usr/bin/env python

import rospy
from my_robot_msgs.srv import ComputeDiskArea

PI = 3.14

def callbackComputDiskArea(req):
    return 2 * PI * req.radius

if __name__ == "__main__":
    rospy.init_node("ComputDiskAreaServer")
    srv = rospy.Service("ComputeDiskArea", ComputeDiskArea, callbackComputDiskArea)
    rospy.spin()

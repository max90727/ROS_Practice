#! /usr/bin/env python
import roslib
roslib.load_manifest('beginner_tutorials')
import rospy
import actionlib

from beginner_tutorials.msg import DoDishesAction, DoDishesGoal

class DoDishesServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('do_dishes', DoDishesAction, self.execute, False)
        self.server.start()

    def execute(self, goal):
        self.server.set_succeeded()

if __name__ == "__main__":
    rospy.init_node('do_dishes_server')
    server = DoDishesServer()
    rospy.spin()
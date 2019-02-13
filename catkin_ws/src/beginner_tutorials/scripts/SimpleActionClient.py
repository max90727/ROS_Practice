#! /usr/bin/env python

import roslib
roslib.load_manifest('beginner_tutorials')
import rospy
import actionlib

from beginner_tutorials.msg import DoDishesAction, DoDishesGoal

if __name__ == "__main__":
    rospy.init_node('do_dishes_client')
    client = actionlib.SimpleActionClient('do_dishes', DoDishesAction)
    client.wait_for_server()

    goal = DoDishesGoal()
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration.from_sec(5.0))
    if client.get_state() == actionlib.SimpleGoalState.DONE:
        rospy.loginfo("Yay! The dishes are now clean")
    else:
        rospy.loginfo("Current State: %s" % client.get_state())
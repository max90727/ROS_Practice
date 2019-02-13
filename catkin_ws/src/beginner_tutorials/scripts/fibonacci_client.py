#! /usr/bin/env python

import rospy
import actionlib
from beginner_tutorials.msg import FibonacciAction, FibonacciGoal

class FibonacciActionClient(object):
    goal = FibonacciGoal()
    def __init__(self, name, goal_value, time_out):
        self._action_name = name
        self._ac = actionlib.SimpleActionClient(self._action_name, FibonacciAction)
        self.goal = FibonacciGoal(goal_value)
        self.time_out = time_out

    def fibonacci_client(self):
        rospy.loginfo('Waiting for action server to start')
        self._ac.wait_for_server()
        rospy.loginfo('Action server started, sending goal.')
        self._ac.send_goal(self.goal)
        finish_before_timeout = self._ac.wait_for_result(rospy.Duration(self.time_out))
        if finish_before_timeout:
            rospy.loginfo('Action finished')
        else:
            rospy.loginfo('Action did not finish before the time out.')
        return self._ac.get_result()

if __name__ == '__main__':
    argv = rospy.myargv()
    if len(argv) != 3:
        rospy.loginfo('Usage: beginner_tutorials fibonacci_client.py <goal> <timeout>')
    else:
        goal = int(argv[1])
        time_out = int(argv[2])
    rospy.init_node('test_fibonacci')
    client = FibonacciActionClient('fibonacci', goal, time_out)
    result = client.fibonacci_client()
    print("Result:", ', '.join([str(n) for n in result.sequence]))
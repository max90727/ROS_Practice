#! /usr/bin/env python

import rospy
import actionlib
from beginner_tutorials.msg import FibonacciAction, FibonacciFeedback, FibonacciResult

class FibonacciActionServer(object):
    _feedback = FibonacciFeedback()
    _result = FibonacciResult()

    def __init__(self, name):
        self.action_name = name
        print("Init name %s" % name)
        self._as = actionlib.SimpleActionServer(self.action_name, FibonacciAction, execute_cb=self.execute_cb, auto_start=False)
        self._as.start()

    def execute_cb(self, goal):
        rate = rospy.Rate(1)
        success = True
        self._feedback.sequence = []
        self._feedback.sequence.append(0)
        self._feedback.sequence.append(1)
        rospy.loginfo('%s: Executing, creating fibonacci sequence of order %i with seed %i, %i'
                      % (self.action_name, goal.order, self._feedback.sequence[0], self._feedback.sequence[1]))

        for i in range(1, goal.order):
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self.action_name)
                self._as.set_preempted()
                success = False
            self._feedback.sequence.append(self._feedback.sequence[i] + self._feedback.sequence[i-1])
            self._as.publish_feedback(self._feedback)
            rate.sleep()

        if success:
            self._result.sequence = self._feedback.sequence
            rospy.loginfo('%s: Succeeded' % self.action_name)
            self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('fibonacci')
    server = FibonacciActionServer('fibonacci')
    rospy.spin()


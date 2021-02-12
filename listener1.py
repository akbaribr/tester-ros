#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def chatterCallback(msg):
    rospy.loginfo('Data diterima : %s', msg.data)

if __name__ == '__main__':
    rospy.init_node('listener_node', anonymous=False)
    rospy.Subscriber('chatter',String,chatterCallback)
    rospy.spin()

#!/usr/bin/env python

import  rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('talker_node', anonymous=False)
    rate = rospy.Rate(1)
    pub = rospy.Publisher('chatter', String,queue_size=10)

    while not rospy.is_shutdown():
        data = 'wkwkwk'
        pub.publish(data)
        rate.sleep()

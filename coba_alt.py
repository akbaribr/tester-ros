#!/usr/bin/env python

import rospy
from mavros_msgs.msg import Altitude
from geometry_msgs.msg import TwistStamped

altitudeData = None

def altCallback(data):
    global altitudeData
    altitudeData = data.local
#    rospy.loginfo("I heard %s", altitudeData)

while not rospy.is_shutdown():
    rospy.init_node('alt_vel_monitor', anonymous=True)
    rospy.Subscriber('mavros/altitude', Altitude, altCallback)
    rospy.sleep(1)

    print altitudeData

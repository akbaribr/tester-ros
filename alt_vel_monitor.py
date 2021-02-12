#!/usr/bin/env python

import rospy
from mavros_msgs.msg import Altitude
from geometry_msgs.msg import TwistStamped
from math import sqrt

altitudeData = None
velx = None
vely = None

def hitung(x, y):
    vel = x**2+y**2
    vel = sqrt(vel)
    return vel

def altCallback(data):
    global altitudeData
    altitudeData = data.local

def velCallback(msg):
    global velx
    global vely

    velx = msg.twist.linear.x
    vely = msg.twist.linear.y

while not rospy.is_shutdown():
    rospy.init_node('alt_vel_monitor', anonymous=True)
    rospy.Subscriber('mavros/altitude', Altitude, altCallback)
    rospy.Subscriber('mavros/global_position/raw/gps_vel', TwistStamped, velCallback)
    rospy.sleep(1)

    v = hitung(velx, vely)

    print 'altitude: ', altitudeData
    print 'velocity: ', '\nx: ', velx, '\ny: ', vely, '\ntotal: ', v

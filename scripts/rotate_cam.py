#!/usr/bin/env python

###########################################
# Andy Zelenak, 2017
# Subscribe for a Vector3Stamped from RViz.
# Rotate a camera to look at that point.
###########################################

# Service definitions
from look_at_pose.srv import *

import rospy
from geometry_msgs.msg import Vector3Stamped


def new_point_cb(pt):
  print( pt )

  # Call the look_at_pose service to get a new camera pose

  # Move the robot to look at that pose

  return

def rotate_cam_server():
  # Subscribe to the Vector3Stamped
  rospy.init_node('rotate_cam_server')
  rospy.Subscriber("/rviz_textured_sphere/pt_of_interest", Vector3Stamped, new_point_cb)
  rospy.spin()

  return

if __name__ == '__main__':
  rotate_cam_server()

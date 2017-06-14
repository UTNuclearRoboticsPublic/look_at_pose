#!/usr/bin/env python

# Andy Zelenak, 2017

# Send test poses to the look_at_pose server
# Print the returned pose, which is a new camera position

#!/usr/bin/env python

from look_at_pose.srv import *

import rospy
import tf

def look_at_pose_client(new_cam_pose, target_pose, up_vector):
    rospy.wait_for_service('look_at_pose')
    try:
        look_at_pose = rospy.ServiceProxy('look_at_pose', LookAtPose)
        new_cam_pose = look_at_pose(new_cam_pose, target_pose, up_vector)
        return new_cam_pose
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    rospy.init_node('test_client')

    # Define the initial camera pose and the target pose to be viewed.
    # Then send them to the service

    # Initial camera pose
    initial_cam_pose = geometry_msgs.msg.PoseStamped()
  
    initial_cam_pose.header.stamp = rospy.Time.now()
    initial_cam_pose.header.frame_id = "ee_frame"
  
    initial_cam_pose.pose.position.x = 0
    initial_cam_pose.pose.position.y = 0
    initial_cam_pose.pose.position.z = 0
  
    #quat = tf.transformations.quaternion_from_euler(0,0,0)
    #initial_cam_pose.pose.orientation.x = quat[0]
    #initial_cam_pose.pose.orientation.y = quat[1]
    #initial_cam_pose.pose.orientation.z = quat[2]
    #initial_cam_pose.pose.orientation.w = quat[3]
    initial_cam_pose.pose.orientation.x = 0
    initial_cam_pose.pose.orientation.y = 0
    initial_cam_pose.pose.orientation.z = 0
    initial_cam_pose.pose.orientation.w = 1

    # For the target pose
    # Should be in the same frame as initial_camera_pose
    target_pose = geometry_msgs.msg.PoseStamped()
    target_pose.header.stamp = rospy.Time.now()
    target_pose.header.frame_id = initial_cam_pose.header.frame_id

    target_pose.pose.position.x = 1.13
    target_pose.pose.position.y = -0.17
    target_pose.pose.position.z = -0.27
  
    #quat = tf.transformations.quaternion_from_euler(0,0,0)
    #target_pose.pose.orientation.x = quat[0]
    #target_pose.pose.orientation.y = quat[1]
    #target_pose.pose.orientation.z = quat[2]
    #target_pose.pose.orientation.w = quat[3]
    initial_cam_pose.pose.orientation.x = 0.39
    initial_cam_pose.pose.orientation.y = -0.45
    initial_cam_pose.pose.orientation.z = -0.53
    initial_cam_pose.pose.orientation.w = 0.595

    # Vector pointing up.
    # Should be in the same frame as initial_camera_pose
    up_vector = geometry_msgs.msg.Vector3Stamped()
    up_vector.header.frame_id = initial_cam_pose.header.frame_id
    up_vector.header.stamp = rospy.Time.now()
    up_vector.vector.x = -0.28  #0
    up_vector.vector.y = -0.109  #0
    up_vector.vector.z = -0.95  #1.0

    # Call the service
    print "new camera pose: %s"% look_at_pose_client(initial_cam_pose, target_pose, up_vector)

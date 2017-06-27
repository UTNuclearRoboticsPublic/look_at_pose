cmake_minimum_required(VERSION 2.8.3)
project(look_at_pose)

find_package(catkin REQUIRED COMPONENTS rospy std_msgs geometry_msgs roscpp message_generation std_srvs)

add_service_files(FILES LookAtPose.srv)

generate_messages(
  DEPENDENCIES
    geometry_msgs
)

catkin_package(CATKIN_DEPENDS roscpp message_runtime INCLUDE_DIRS)

include_directories(${catkin_INCLUDE_DIRS})
link_directories(${catkin_LIBRARY_DIRS})

#############
## Install ##
#############

catkin_install_python(PROGRAMS nodes/look_at_pose_server nodes/test_client
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

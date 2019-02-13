#!/bin/bash

#initialize rosdep
INIT=$(rosdep init)
if [[ $INIT == *"rosdep update"* ]]; then
  rosdep update
else
  echo "rosdep init failed!"
fi

echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
if [ -f "/data/catkin_ws/devel/setup.bash" ]; then
  echo "source /data/catkin_ws/devel/setup.bash" >> ~/.bashrc
fi
# For local test
export ROS_HOSTNAME=localhost
export ROS_MASTER_URI=http://localhost:11311
source ~/.bashrc
$@
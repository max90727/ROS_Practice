#!/bin/bash

# exit on fail
set -e

apt_install="apt-get install -y --no-install-recommends"
pip_install="pip install --upgrade"
key_install="apt-key "
dpkg --add-architecture i386
apt-get update
$apt_install software-properties-common
$apt_install wget
# setup sources.list
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
# Setup keys
$key_install adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
#installation
apt-get update
$apt_install ros-kinetic-desktop-full

#dependencies for building packages
$apt_install python-rosinstall python-rosinstall-generator python-wstool build-essential


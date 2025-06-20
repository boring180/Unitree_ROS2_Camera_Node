# Unitree_ROS2_Camera_Node

## Background
This is a ROS2 package developed for the Unitree GO2 robot. It is built in the UNSW Robotics Lab.

## Features
- This node is to connect the camera on the Unitree GO2 robot to the ROS2 system.
- It can output the camera image as a ROS2 image topic. And further read by RVIZ2.

## Installation

### Install the ROS2 environment
Please refer to the [ROS2 installation guide](https://docs.ros.org/en/humble/Installation.html) to install the ROS2 environment.

### Install Unitree ROS2
Please refer to the [Unitree ROS2 installation guide](https://github.com/unitreerobotics/unitree_ros2) to install the Unitree ROS2.

### Install Unitree Python SDK2
Please refer to the [Unitree Python SDK2 installation guide](https://github.com/unitreerobotics/unitree_sdk2_python) to install the Unitree Python SDK2.

### Install neccessary python libraries
```bash
pip install -r requirements.txt
```

## Usage

### Run the camera node
```bash
ros2 run cv cv_node
```

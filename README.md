## 搭建UR5+robotiq2f_85+realsense D455 URDF

### 环境配置
1. 系统环境配置
- ubuntu24.04

2. 软件环境配置
- ros2 jazzy


### 编译
1. 下载当前仓库代码
```
git clone git@github.com:WAI-f/ur_robotiq_realsense_description.git
git submodule update --init --recursive
```
2. 编译代码
```
cd ur_robotiq_realsense_description
colcon build
```

### 可视化



### 说明
- UR description参考仓库：[Universal_Robots_ROS2_Description](https://github.com/UniversalRobots/Universal_Robots_ROS2_Description/tree/jazzy)


- robotiq_gripper参考仓库：[ros2_robotiq_gripper](https://github.com/PickNikRobotics/ros2_robotiq_gripper/tree/main)

- realsense参考仓库：[realsense-ros](https://github.com/realsenseai/realsense-ros/tree/ros2-master)
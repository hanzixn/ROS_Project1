# Ros
准备工作
首先确保已经安装了ROS Melodic(Ubuntu 18.04对应的ROS版本)和turtlesim包：
sudo apt-get install ros-melodic-ros-tutorials ros-melodic-turtlesim

创建并初始化工作空间：
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make

设置工作空间环境变量：
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc

创建ROS包：
cd ~/catkin_ws/src
catkin_create_pkg turtle_control rospy geometry_msgs turtlesim

创建scripts目录并编写代码：
mkdir -p ~/catkin_ws/src/turtle_control/scripts
cd ~/catkin_ws/src/turtle_control/scripts
gedit turtle_controller.py


给脚本添加可执行权限：
chmod +x turtle_controller.py

构建工作空间
cd ~/catkin_ws
catkin_make

运行实验：
终端1 - 运行ROS核心服务：
roscore
终端2 - 运行turtlesim仿真器：
rosrun turtlesim turtlesim_node
终端3 - 运行控制器节点：
cd ~/catkin_ws
source devel/setup.bash
rosrun turtle_control turtle_controller.py

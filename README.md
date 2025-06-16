markdown
复制
下载
# ROS TurtleSim 控制实验

## 📦 准备工作

### 安装依赖
确保已安装 ROS Melodic (Ubuntu 18.04) 和 turtlesim 包：
```bash
sudo apt-get install ros-melodic-ros-tutorials ros-melodic-turtlesim
🏗 创建工作空间
bash
复制
下载
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
⚙ 设置环境变量
bash
复制
下载
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc    
source ~/.bashrc 
🛠 创建ROS包
bash
复制
下载
cd ~/catkin_ws/src    
catkin_create_pkg turtle_control rospy geometry_msgs turtlesim
📝 编写控制器
创建scripts目录：
bash
复制
下载
mkdir -p ~/catkin_ws/src/turtle_control/scripts    
cd ~/catkin_ws/src/turtle_control/scripts    
创建Python脚本：
bash
复制
下载
gedit turtle_controller.py
添加可执行权限：
bash
复制
下载
chmod +x turtle_controller.py
🔨 构建工作空间
bash
复制
下载
cd ~/catkin_ws
catkin_make
🚀 运行实验
需要开启三个终端窗口：
终端命令说明
1 roscore 启动ROS核心服务 
2 rosrun turtlesim turtlesim_node 启动turtlesim仿真器 
3 cd ~/catkin_ws && source devel/setup.bash && rosrun turtle_control turtle_controller.py 运行控制器节点 
💡 提示：确保每个命令都在正确的目录下执行

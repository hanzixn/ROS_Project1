#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


class TurtleController:
    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)

        # 目标点坐标
        self.goal_x = 4.0
        self.goal_y = 4.0

        # 当前海龟位置
        self.current_x = 0
        self.current_y = 0
        self.current_theta = 0

        # 发布速度指令
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        # 订阅海龟当前位置
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        self.rate = rospy.Rate(10)  # 控制频率10Hz

    def update_pose(self, data):
        """更新海龟当前位置"""
        self.current_x = data.x
        self.current_y = data.y
        self.current_theta = data.theta

    def euclidean_distance(self, goal_x, goal_y):
        """计算与目标点的距离"""
        return math.sqrt(math.pow((goal_x - self.current_x), 2) + math.pow((goal_y - self.current_y), 2))

    def linear_vel(self, goal_x, goal_y, constant=1.5):
        """计算线速度"""
        return constant * self.euclidean_distance(goal_x, goal_y)

    def steering_angle(self, goal_x, goal_y):
        """计算需要转向的角度"""
        return math.atan2(goal_y - self.current_y, goal_x - self.current_x)

    def angular_vel(self, goal_x, goal_y, constant=6):
        """计算角速度"""
        return constant * (self.steering_angle(goal_x, goal_y) - self.current_theta)

    def move2goal(self):
        """移动海龟到目标点的主函数"""
        goal_pose = Pose()
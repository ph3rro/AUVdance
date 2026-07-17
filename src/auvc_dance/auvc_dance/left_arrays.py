import time
import rclpy    # the ROS 2 client library for Python
from rclpy.node import Node    # the ROS 2 Node class

class Left:
    def go_left(secs, strength):
        neutral = 500
        return [0.5, neutral + strength, neutral, neutral, neutral]
    
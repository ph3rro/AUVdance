import time
from geometry_msgs.msg import Twist
import rclpy    # the ROS 2 client library for Python
from rclpy.node import Node    # the ROS 2 Node class
import numpy as np

class Claps:
    def clap_once():
        movement_arr = [0.0, 0.0, 0.5, 0.0, 0.0, 0.0]
        return movement_arr
    
    def stop():
        return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    

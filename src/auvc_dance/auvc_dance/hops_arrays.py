import time
import rclpy    # the ROS 2 client library for Python
import numpy as np

class Claps:
    def hop_once():
        movement_arr = [0.0, 0.0, 0.75, 0.0, 0.0, 0.0]
        return movement_arr
    
    def stop():
        return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    

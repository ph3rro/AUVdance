import time
from geometry_msgs.msg import Twist
import rclpy    # the ROS 2 client library for Python
from rclpy.node import Node    # the ROS 2 Node class
import numpy as np
from claps import Claps

class DanceNode(Node):
    def __init__(self):
        super().__init__("dance_node")    # names the node when running

        # Setting up the publishing topic
        self.dance_moves = self.create_publisher(Twist, "dance_moves", 10)

        #DANCE 
        self.timer = self.create_timer(1.0, self.move_callback(Claps.clap_once()))
        self.timer = self.create_timer(1.0, self.move_callback(Claps.stop()))



    # This is just called every timer to upload a movement array to the topic
    def move_callback(self, arr):
        msg = Twist

        msg.linear.x = arr[0]
        msg.linear.y = arr[1]
        msg.linear.z = arr[2]

        msg.angular.x = arr[3]
        msg.angular.y = arr[4]
        msg.angular.z = arr[5]

        self.dance_moves.publish(msg)
        self.get_logger().info(f'Publishing: {arr}')




def main(args=None):
    rclpy.init(args=args)
    node = DanceNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

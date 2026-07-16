
import rclpy
from rclpy.node import Node

import numpy as np
import sys


class VirtualEnvironmentsTutorial(Node):
    """
    This node demonstrates how ROS 2 packages can be compiled to run executables in a virtual environment.
    """
    def __init__(self):
        super().__init__("tutorial_virtualenvs")

        self.declare_parameter("theta", 3.14159)    # parameter name and default value in radians

        self.theta = self.get_parameter("theta").value
        self.get_logger().info(sys.executable)


    def run(self):
        """
        This method logs the sin of the theta parameter using the numpy library to the terminal.
        """
        solution = np.sin(self.theta)
        self.get_logger().info(f"sin({self.theta}) = {solution}")


def main(args=None):
    rclpy.init(args=args)
    node = VirtualEnvironmentsTutorial()

    try:
        node.run()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
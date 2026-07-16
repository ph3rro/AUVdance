import rclpy    # the ROS 2 client library for Python
from rclpy.node import Node    # the ROS 2 Node class
from geometry_msgs.msg import Vector3    # the Vector3 message type definition

class tutorial_subscriber(Node):
    def __init__(self):
        
        super().__init__("tutorial_subscriber")    # names the node when running

        self.sub = self.create_subscription(
            Vector3,        # the message type
            "/tutorial",    # the topic name
            self.log_vector3,    # callback function
            10              # QOS (will be covered later)
        )

        self.get_logger().info("initialized subscriber node")

    def log_vector3(self, msg):
        magnitude = (msg.x**2 + msg.y**2 + msg.z**2)**0.5
        self.get_logger().info(f"magnitude {magnitude}")

def main(args=None):
    rclpy.init(args=args)
    node = tutorial_subscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
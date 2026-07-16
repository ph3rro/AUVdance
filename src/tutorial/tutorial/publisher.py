import rclpy    # the ROS 2 client library for Python
from rclpy.node import Node    # the ROS 2 Node class
from geometry_msgs.msg import Vector3    # the Vector3 message type definition


class tutorial_publisher (Node):
    def __init__(self):
        super().__init__("tutorial_publisher")    # names the node when running

        self.pub = self.create_publisher(
            Vector3,        # the message type
            "/tutorial",    # the topic name
            10              # QOS (will be covered later)
        )

        self.timer = self.create_timer(
            1.0,    # timer period (sec)
            self.publish_vector3    # callback function
        )

        self.get_logger().info("initialized publisher node")
    def publish_vector3(self):
        msg = Vector3()
        msg.x = 4.0
        msg.y = 3.0
        msg.z = 5.0
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = tutorial_publisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

        
    
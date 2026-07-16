import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState
from sensor_msgs.msg import Imu

class Sensors(Node):
    def __init__(self):
        super().__init__("bluerov2_sensors")
        self.battery_sub = self.create_subscription(
            BatteryState,
            "/battery_state",
            self.battery_state_callback,
            10
        )
        self.imu_sub = self.create_subscription(
            Imu,
            "/imu",
            self.imu_callback,
            10
        )
    def battery_state_callback(self, msg):
        SAFE_VOLTAGE = 12
        if (msg.voltage < SAFE_VOLTAGE):
            self.get_logger().info("Unsafe Voltage detected!")
        self.get_logger().info(f"Voltage: {msg.voltage}")
    def imu_callback(self,msg):
        self.get_logger().info(f"X ang vel: {msg.angular_velocity.x}")

def main(args=None):
    rclpy.init(args=args)
    node = Sensors()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

        
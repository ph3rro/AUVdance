import rclpy
from rclpy.node import Node
from mavros_msgs.msg import ManualControl

class Arming(Node):
  def __init__(self):
    super().__init__("arming_node")
    self.arming_service = self.create_service(SetBool, "arming", self.arming_callback)

  def arming_callback(self, request, response):
    """
    Callback for the arming service.
    """
    if request.data:
      self.mavlink.arducopter_arm()
    else:
      self._set_neutral_all_channels()
      self.mavlink.arducopter_disarm()
    response.success = True
    response.message = f"Arming: {request.data}"
    return response

def main(args=None):
  rclpy.init(args=args)
  node = Arming()

  try:
      self.mavlink.arducopter_arm()
  except KeyboardInterrupt:
      print("\nKeyboardInterrupt received, shutting down...")
      node.mavlink.arducopter_disarm()
  finally:
      node.destroy_node()
      if rclpy.ok():
          rclpy.shutdown()

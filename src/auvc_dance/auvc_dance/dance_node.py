import rclpy
from rclpy.node import Node
from mavros_msgs.msg import ManualControl
import time
import numpy as np
from auvc_dance.hops_arrays import *
from auvc_dance.left_arrays import *
from auvc_dance.right_arrays import *
from auvc_dance.back_arrays import *

class DanceNode(Node):
    def __init__(self):
        super().__init__('rov_choreographer')
        
        '''self.manual_pub publishes the movements so the auv can read them'''
        self.manual_pub = self.create_publisher(ManualControl, '/manual_control', 10)
        
        '''self.dance_routine is an array of arrays that dictates the dance routine'''
        # heave is from 0 to 1000, where 500 is neutral, 0 is down, and 1000 is up
        # surge is forward backward, sway is left to right, heave is up and down, yaw is turn
        neutral = 50.0
        self.dance_routine = [
            [1.75, 0, 0, neutral, 0],
            hop(0.5, 25.0), # duration, strength/500
            [1.5, 0, 0, neutral, 0],
            right(0.5, 40.0),
            [1.5, 0, 0, neutral, 0],
            left(0.5, 30.0),
            #hop(3.5, 0.0, 500.0),
            #[2.0, 0, 0, neutral, 0],
            #right(0.5, 500.0),
            #[1.5, 0, 0, neutral, 0],
            #left(0.5, 500.0),
            #[1.5, 0, 0, neutral, 0],
            #back(0.5, 500.0),
            #[1.5, 0, 0, neutral, 0],
            #hop(0.5, 500.0),
            #[1.5, 0, 0, neutral, 0],
            #hop(0.5, 500.0),
            #[1.5, 0, 0, neutral, 0],
            #diagonal_right(1.0, 200.0, 500.0),
            #[1.0, 0, 0, neutral, 0],
            #diagonal_left(1.0, 200.0, 500.0),
            #[1.0, 0, 0, neutral, 0],
            #left(0.5, 500),
            #[1.0, 0, 0, neutral, 0],
            #right(0.5, 500.0),
            #[1.5, 0, 0, neutral, 0],
            #diagonal_right(3.0, 200.0, 600.0), #change to diagonal_left for other auv
            # CIRCLE
        ]
        
        
        self.current_step_index = 0
        self.elapsed_time_in_step = 0.0
        
        # run loop at 20 hz
        self.timer_period = 0.05
        self.timer = self.create_timer(self.timer_period, self.execute_routine)
        
        self.get_logger().info("Choreography Node Started. Beginning routine...")

    def execute_routine(self):
        if self.current_step_index >= len(self.dance_routine):
            self.send_neutral_command()
            return

        duration, surge, sway, heave, yaw = self.dance_routine[self.current_step_index]

        # Publish the active step's joystick values
        msg = ManualControl()
        msg.x = float(surge)
        msg.y = float(sway)
        msg.z = float(heave)
        msg.r = float(yaw)
        self.manual_pub.publish(msg)

        # Track progress
        self.elapsed_time_in_step += self.timer_period

        # Time's up! Transition to the next move
        if self.elapsed_time_in_step >= duration:
            self.get_logger().info(f"Finished step {self.current_step_index + 1}/{len(self.dance_routine)}")
            self.current_step_index += 1
            self.elapsed_time_in_step = 0.0  # Reset clock for next move
            
            if self.current_step_index < len(self.dance_routine):
                self.get_logger().info(f"Starting next step: {self.dance_routine[self.current_step_index]}")
            else:
                self.get_logger().info("Dance finished!")
                self.send_neutral_command()
                self.timer.cancel()

    def send_neutral_command(self):
        msg = ManualControl()
        msg.x, msg.y, msg.r = 0.0, 0.0, 0.0
        msg.z = 500.0 
        self.manual_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DanceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.send_neutral_command()
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

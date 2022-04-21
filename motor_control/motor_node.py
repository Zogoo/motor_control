import rclpy
from rclpy.node import Node

from motor_control.controller import Controller

class MotorNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hello ROS2")
        self.create_timer(0.5, self.timer_callback)
    
    def timer_callback(self):
        self.get_logger().info("Hello")

def main(args=None):
    rclpy.init(args=args)
    node = MotorNode()
    node.get_logger().info("Hello ROS2")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
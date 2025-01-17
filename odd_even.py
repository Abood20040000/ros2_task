#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class OddEven(Node):
    def __init__(self):
        super().__init__("oddeven")
        self.counter_=0
        self.create_timer(1.0,self.ckeck_Odd_Even)


    def ckeck_Odd_Even(self):
        if (self.counter_%2==0):
            self.get_logger().info(f"the number {self.counter_} is even")
        else:
            self.get_logger().info(f"the number {self.counter_} is odd")

        self.counter_+= 1   


def main(args=None):
    rclpy.init(args=args)
    node=OddEven()
    rclpy.spin(node)
    rclpy.shutdown()

if (__name__=='__main__'):
    main()                     

#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import random

class Data_collection(Node):
    def __init__(self):
        super().__init__("data")
        self.temp=0
        self.pressure=0
        self.humidity=0
        self.create_timer(1.0,self.Mydata)

    
    def Mydata(self):
        self.temp=random.randint(20,40)
        self.pressure=random.randint(100,200)
        self.humidity=random.randint(0,100)
        self.get_logger().info(f"the temp is {self.temp} , the pressure is {self.pressure} and the humidity is {self.humidity} ")



def main(args=None):
    rclpy.init(args=args)
    node=Data_collection()
    rclpy.spin(node)
    rclpy.shutdown()

if (__name__=='__main__'):
    main()    
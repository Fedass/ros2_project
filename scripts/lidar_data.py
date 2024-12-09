import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math
import csv
import os

class LidarToDataset(Node):
    def __init__(self):
        super().__init__('lidar_to_dataset')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            10)
        self.subscription 

        self.dataset_file = 'lidar_dataset.csv'
        self.init_csv()

    def init_csv(self):
        with open(self.dataset_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['x', 'y', 'distance'])

    def lidar_callback(self, msg):
        angle_min = msg.angle_min
        angle_increment = msg.angle_increment
        ranges = msg.ranges

        with open(self.dataset_file, mode='a', newline='') as file:
            writer = csv.writer(file)

            for i, r in enumerate(ranges):
                if r < float('inf'): 
                    angle = angle_min + i * angle_increment
                    x = r * math.cos(angle)
                    y = r * math.sin(angle)
                    writer.writerow([x, y, r])

        self.get_logger().info(f"Записаны данные в {self.dataset_file}")

def main(args=None):
    rclpy.init(args=args)
    node = LidarToDataset()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


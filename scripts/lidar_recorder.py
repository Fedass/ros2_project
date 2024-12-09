import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import numpy as np
import cv2
import math
from datetime import datetime

class LidarVideoRecorder(Node):
    def __init__(self):
        super().__init__('lidar_video_recorder')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            10)
        self.subscription 

        self.video_filename = f'lidar_video_{datetime.now().strftime("%Y%m%d_%H%M%S")}.avi'
        self.frame_width = 640
        self.frame_height = 640
        self.fps = 10

        self.out = cv2.VideoWriter(
            self.video_filename,
            cv2.VideoWriter_fourcc(*'XVID'),
            self.fps,
            (self.frame_width, self.frame_height)
        )

        self.get_logger().info(f"Запись видео начата: {self.video_filename}")

    def lidar_callback(self, msg):
        frame = np.zeros((self.frame_width, self.frame_height, 3), dtype=np.uint8)
        center_x, center_y = self.frame_width // 2, self.frame_height // 2

        angle_min = msg.angle_min
        angle_increment = msg.angle_increment
        ranges = msg.ranges

        for i, r in enumerate(ranges):
            if r < float('inf'):  
                angle = angle_min + i * angle_increment
                x = int(center_x + r * 100 * math.cos(angle))
                y = int(center_y - r * 100 * math.sin(angle))
                if 0 <= x < self.frame_width and 0 <= y < self.frame_height:
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)

        self.out.write(frame)

    def destroy_node(self):
        self.out.release()
        self.get_logger().info(f"Запись видео завершена: {self.video_filename}")
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = LidarVideoRecorder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


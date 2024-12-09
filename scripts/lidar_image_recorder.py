import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from datetime import datetime

class CameraVideoRecorder(Node):
    def __init__(self):
        super().__init__('camera_video_recorder')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw', 
            self.image_callback,
            10)
        self.subscription 

        self.video_filename = f'camera_video_{datetime.now().strftime("%Y%m%d_%H%M%S")}.avi'
        self.bridge = CvBridge()
        self.fps = 10  
        self.frame_size = (640, 480) 
        self.out = cv2.VideoWriter(
            self.video_filename,
            cv2.VideoWriter_fourcc(*'XVID'),
            self.fps,
            self.frame_size
        )

        self.get_logger().info(f"Запись видео начата: {self.video_filename}")

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            self.out.write(frame)  # Запись кадра в видео
        except Exception as e:
            self.get_logger().error(f"Ошибка обработки кадра: {e}")

    def destroy_node(self):
        self.out.release()
        self.get_logger().info(f"Запись видео завершена: {self.video_filename}")
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = CameraVideoRecorder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()


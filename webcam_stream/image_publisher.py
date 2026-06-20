import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisher(Node):
    def __init__(self):
        super(). __init__('image_publisher')
        self.cap = cv2.VideoCapture(0)
        self.publisher_ = self.create_publisher(Image, 'Webcam', 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)
        self.br = CvBridge()
        self.get_logger().info("Publisher Node Initialized")

    def timer_callback(self):
        succ, frame = self.cap.read()
        if succ:
            self.get_logger().info("Successfully Capture Image")
            self.publisher_.publish(self.br.cv2_to_imgmsg(frame, encoding='bgr8'))
        else:
            self.get_logger().info("Failed To Capture Image")

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()

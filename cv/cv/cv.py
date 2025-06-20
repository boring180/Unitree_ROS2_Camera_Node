import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge  # Convert OpenCV image to ROS2 Image message
from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.go2.video.video_client import VideoClient
import cv2
import numpy as np
import os
import xml.etree.ElementTree as ET

def get_network_interface_name():
    """Extract network interface name from CYCLONEDDS_URI environment variable"""
    cyclonedds_uri = os.environ.get('CYCLONEDDS_URI')
    if not cyclonedds_uri:
        return None
    
    try:
        # Parse the XML content
        root = ET.fromstring(cyclonedds_uri)
        
        # Find the NetworkInterface element and get its name attribute
        network_interface = root.find('.//NetworkInterface')
        if network_interface is not None:
            return network_interface.get('name')
        else:
            return None
    except ET.ParseError as e:
        print(f"Error parsing CYCLONEDDS_URI XML: {e}")
        return None

class CVNode(Node):
    def __init__(self):
        super().__init__("cv_node")
        self.publisher_ = self.create_publisher(Image, "/front_camera/image_raw", 10)
        self.bridge = CvBridge()
        
        # Get network interface name
        network_interface = get_network_interface_name()
        if network_interface:
            self.get_logger().info(f"Using network interface: {network_interface}")
        else:
            self.get_logger().warning("Could not extract network interface name from CYCLONEDDS_URI")
        
        ChannelFactoryInitialize(0, network_interface)
        self.client = VideoClient()
        self.client.SetTimeout(3.0)
        self.client.Init()

        code, data = self.client.GetImageSample()

        # Request normal when code==0
        while code == 0:
            code, data = self.client.GetImageSample()

            image_data = np.frombuffer(bytes(data), dtype=np.uint8)
            image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

            self.publisher_.publish(self.bridge.cv2_to_imgmsg(image))


def main(args=None):
    rclpy.init(args=args)
    cv_node = CVNode()
    rclpy.spin(cv_node)

    cv_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
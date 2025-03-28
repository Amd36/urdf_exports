from launch import LaunchDescription
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_name = 'robotic_arm_urdf'  # Replace with actual package name
    urdf_file = 'urdf/robotic_arm_urdf.urdf'
    rviz_config_file = 'urdf.rviz'

    urdf_path = os.path.join(get_package_share_directory(package_name), urdf_file)
    rviz_path = os.path.join(get_package_share_directory(package_name), rviz_config_file)

    return LaunchDescription([
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': open(urdf_path).read()}],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_path],
        ),
    ])

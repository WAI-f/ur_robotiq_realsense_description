from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os
import xacro

def generate_launch_description():

    pkg_path = get_package_share_directory(
        'ur5_robotiq85_rsd455_description'
    )

    xacro_file = os.path.join(
        pkg_path,
        'urdf',
        'ur5_robotiq85_rsd455.urdf.xacro'
    )

    robot_description = xacro.process_file(
        xacro_file
    ).toxml()

    return LaunchDescription([

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': robot_description
            }]
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])
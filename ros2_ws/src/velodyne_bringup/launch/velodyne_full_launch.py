import os
from datetime import datetime

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Launch argument for rosbag output directory
    bag_dir = LaunchConfiguration("bag_dir")

    # Locate the VLP-16 calibration file from the installed
    # velodyne_pointcloud package.
    velodyne_pointcloud_share = get_package_share_directory(
        "velodyne_pointcloud"
    )
    calibration_file = os.path.join(
        velodyne_pointcloud_share,
        "params",
        "VLP16db.yaml",
    )

    # Generate a timestamped recording directory.
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    full_bag_path = os.path.join(
        bag_dir,
        f"velodyne_bag_{timestamp}",
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "bag_dir",
                default_value=os.path.expanduser(
                    "~/velodyne_bags"
                ),
                description=(
                    "Directory where timestamped rosbag2 "
                    "recordings will be stored."
                ),
            ),

            # Velodyne driver
            Node(
                package="velodyne_driver",
                executable="velodyne_driver_node",
                name="velodyne_driver_node",
                parameters=[
                    {
                        "device_ip": "192.168.1.201",
                        "frame_id": "velodyne",
                        "model": "VLP16",
                        "port": 2368,
                        "read_once": False,
                        "read_fast": False,
                        "repeat_delay": 0.0,
                        "cut_angle": -0.01,
                        "gps_time": False,
                        "timestamp_first_packet": False,
                    }
                ],
                output="screen",
            ),

            # Convert Velodyne packets into PointCloud2 messages
            Node(
                package="velodyne_pointcloud",
                executable="velodyne_transform_node",
                name="velodyne_transform_node",
                parameters=[
                    {
                        "calibration": calibration_file,
                        "model": "VLP16",
                    }
                ],
                remappings=[
                    ("velodyne_packets", "/velodyne_packets")
                ],
                output="screen",
            ),

            # Static transform: base_link -> velodyne
            Node(
                package="tf2_ros",
                executable="static_transform_publisher",
                name="velodyne_static_tf",
                arguments=[
                    "0",
                    "0",
                    "0",
                    "0",
                    "0",
                    "0",
                    "base_link",
                    "velodyne",
                ],
                output="screen",
            ),

            # Record raw packets, point clouds, and static TF
            ExecuteProcess(
                cmd=[
                    "ros2",
                    "bag",
                    "record",
                    "/velodyne_packets",
                    "/velodyne_points",
                    "/tf_static",
                    "--output",
                    full_bag_path,
                ],
                output="screen",
            ),
        ]
    )

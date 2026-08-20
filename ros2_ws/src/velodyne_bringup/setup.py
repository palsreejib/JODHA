from setuptools import find_packages, setup

package_name = "velodyne_bringup"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(include=[package_name, package_name + ".*"]),
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resource/" + package_name],
        ),
        (
            "share/" + package_name,
            ["package.xml"],
        ),
        (
            "share/" + package_name + "/launch",
            ["launch/velodyne_full_launch.py"],
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Sreejib Pal",
    maintainer_email="sreejib1945@gmail.com",
    description=(
        "ROS 2 bringup package for Velodyne VLP-16 "
        "LiDAR data acquisition and rosbag2 recording."
    ),
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)

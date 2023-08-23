# Sentinel-Drone
**Sentinel Drone Project - Eyantra**

The Sentinel Drone project is an autonomous drone system designed to detect and hover over a yellow block placed in an aerial image. The project utilizes QGIS software, ROS, Gazebo, and OpenCV to achieve its objectives.

**Project Structure:**

- `aerial_modified_sub.tif`: This modified .tgif image file contains an aerial view of the environment with a yellow block placed in it. It serves as the input for block detection and hovering tasks.

- `block_detection.py`: This Python script is responsible for detecting the yellow block within the aerial image. The script identifies the center coordinates of the detected block, which are used for drone hovering.

- `position_hold.py`: The position_hold module ensures autonomous hovering of the drone. It employs PID controllers to maintain the drone's position over the center of the yellow block. The drone's simulation takes place in Gazebo using ROS.

- `requirements.txt`: The requirements file lists all the necessary libraries and dependencies required to run the `task2b.py` script.

- `result-2022-SD-0-20220922.json`: This JSON file is generated after setting up the required repositories and configuring the computer for the project.

- `task2b.py`: The task2b Python script uses OpenCV to detect the center of the yellow block within the aerial image.

- `waypoint_navigation.py`: This module handles the drone's navigation through specified waypoints, enabling it to move autonomously along a predefined path.

**Usage:**

1. Install QGIS software and open the `aerial_modified_sub.tif` image.

2. Execute `block_detection.py` to detect the yellow block in the aerial image and obtain its center coordinates.

3. Ensure your drone hardware is ready for autonomous flight.

4. Run the Gazebo simulation using ROS and execute `position_hold.py` with the tuned PID values to enable the drone to hover over the detected yellow block's center.

5. To run `task2b.py`, ensure all the libraries listed in `requirements.txt` are installed. This script detects the center of the yellow block using OpenCV.

6. Implement `waypoint_navigation.py` to enable the drone to autonomously navigate through specified waypoints.

**Note:**

Accurate block detection and precise hovering algorithms are crucial for the success of the Sentinel Drone project. Proper calibration and tuning of PID controllers are necessary for stable hovering.

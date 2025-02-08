# Localização Robótica
Trabalho apresentado na disciplina de Localização Robótica no curso de Engenharia Elétrica da UBFA

Pacotes utilizados:
https://github.com/PXLRoboticsLab/ardrone_gazebo
https://github.com/niobegrzegorzdec/lsd_slam
https://github.com/lar-deeufba/lar_gazebo

1° Terminal
source ~/projeto_ws/devel/setup.bash

roslaunch lar_gazebo lar_ardrone_drone.launch

2° Terminal
rosrun teleop_twist_keyboard teleop_twist_keyboard.py

3° Terminal
rosrun lsd_slam_core live_slam /image:=/ardrone/front_camera/image_raw /camera_info:=/ardrone/camera_info

![SLAM_teste](https://github.com/user-attachments/assets/fd59780c-473a-4f47-879e-df0910f8844e)

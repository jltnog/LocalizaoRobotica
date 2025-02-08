#!/usr/bin/env python3

import rospy
import tf
from geometry_msgs.msg import PoseStamped
import rosbag

# Inicialize o nó ROS
rospy.init_node('pose_transformer')

# Crie um listener para ouvir as transformações
listener = tf.TransformListener()

def transform_pose_to_robot_frame(pose_in_world):
    try:
        # Aguarde até que a transformação entre "map" e "base_link" esteja disponível
        listener.waitForTransform("base_link", "map", rospy.Time(0), rospy.Duration(4.0))
        
        # Transforme a pose do referencial "map" para o referencial "base_link" (do robô)
        pose_in_robot = listener.transformPose("base_link", pose_in_world)

        return pose_in_robot
    except (tf.Exception, tf.LookupException, tf.ConnectivityException, tf.TransformException) as e:
        rospy.logerr("Erro ao realizar a transformação TF: %s", str(e))
        return None

def process_bag_file(bag_file):
    # Abra o arquivo .bag
    bag = rosbag.Bag(bag_file, 'r')

    # Itere sobre as mensagens do tópico de pose (exemplo: /amcl_pose)
    for topic, msg, t in bag.read_messages(topics=['/lsd_slam/pose']):
        # Transforme a pose de "map" para "base_link"
        pose_in_robot = transform_pose_to_robot_frame(msg)

        if pose_in_robot:
            rospy.loginfo("Pose transformada para o referencial do robô: %s", pose_in_robot)

    # Feche o arquivo .bag
    bag.close()

if __name__ == "__main__":
    # Substitua '<seu_arquivo.bag>' pelo caminho do arquivo .bag
    process_bag_file('/home/joao/Documents/Semestre 2024.2/Localiza├з├гo Rob├│tica/Projeto Semestral/BAGS/teste_projeto.bag')


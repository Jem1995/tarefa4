import rospy
from std_msgs.msg import String

rospy.init_node('Soma')


def CB(msg):  # Recebe a matricula e calcula a soma
    somar = 0
    for a in range(len(msg.data)):
        somar = somar + int(msg.data[a])
    msg.data = str(somar)
    pub.publish(msg)


pub = rospy.Publisher('/Soma', String, queue_size=10)
sub = rospy.Subscriber('/matricula', String, CB)

rospy.spin()
import rospy
from std_msgs.msg import String
    
rospy.init_node('matricula')

somar = String()
matricula = String()
       
def FunCallBack (msg):
    global somar
    somar = msg
    print ("Soma dos numeros da matricula: " + somar.data)
    
def Timer(msg):
    msg = String()
    msg.data = '2017020094'
    print ("Numero da Matricula: " + msg.data)
  
    pub.publish(msg) 

pub = rospy.Publisher ('/matricula', String, queue_size =10)
sub = rospy.Subscriber('/Soma', String,FunCallBack)
timer = rospy.Timer(rospy.Duration(1),Timer)

rospy.spin()
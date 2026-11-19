import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.msg import Person   #通信の型（16ビットの符号付き整数）

rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Person, "person", 10)   #パブリッシャ作成（型、トピック名、キュー長）
n = 0

def cb():
    global n
    msg = Person()          #変更: Person型のメッセージを作る
    msg.name = "本山暖"    #変更: msgファイルに書いた「name」
    msg.age = n % 256       #変更: msgファイルに書いた「age」（0〜255まで）
    pub.publish(msg)
    n += 1



def main():
    node.create_timer(0.5, cb)  #0.5秒ごとにcbを呼ぶタイマー
    rclpy.spin(node)            #実行（無限ループ。タイマーや送受信を処理し続ける）

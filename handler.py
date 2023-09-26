import requests
import tool.AutoGUI as g
from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/', methods=["POST"])
def post_data():
    p='0'
    print(request.get_json())
    if request.get_json().get('message_type') == 'private': 
        # 获取需要的消息
        QQ_id = request.get_json().get('sender').get('user_id')           # 发送者的QQ号
        Xingxi_text = request.get_json().get('raw_message')               # 发的什么东西

        # 处理消息
        if Xingxi_text == "电脑截屏":
            # 发送送信息
            url = "http://127.0.0.1:5700/send_private_msg"
            params = {
                "user_id": QQ_id,
                "message": "正在帮你截屏。。。"
                }
            requests.get(url=url, params=params)

            # 截图并保存
            if g.Store_Scene():
                # 发送消息
                params = {
                "user_id": QQ_id,
                "message": "[CQ:image,file=scene.png]"
                }
            requests.get(url=url, params=params)
    return p
 
app.run(debug=True, host='127.0.0.1', port=5701)
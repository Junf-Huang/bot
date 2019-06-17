import itchat, time
from itchat.content import *
import logging
#logging.basicConfig(filename='sample.log',level=logging.DEBUG,format = '%(asctime)s:%(name)s:%(message)s')


def after_login():
    logging.info("已登录")
    # 通过微信号查找好友
    user_info = itchat.search_friends(wechatAccount='gt840cpui5')
    if len(user_info) > 0:
        user_name = user_info[0]['UserName']
        itchat.send_msg('Bot login!', user_name)
    # 通过群聊名查找
    logging.debug("chatroomList:", itchat.get_chatrooms())
    chat_rooms = itchat.search_chatrooms(name='小家庭小故事')
    if len(chat_rooms) > 0:
        #itchat.send_msg('机器人已登录，欢迎大家的调戏', chat_rooms[0]['UserName'])

def after_logout():
    logging.info("退出后调用")

# 图灵机器人
def tuling_reply(msg):
    appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    req = requests.get(url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer

# 私聊回复
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    logging.debug("received message: %s", msg)
    # 发送消息
    itchat.send_msg('%s' % msg.text, msg['FromUserName'])

# 群聊回复
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    # 如果被@到，则回复
    if msg.isAt:
        itchat.send_msg("接受{0}的消息内容：{1}".format(msg['ActualNickName'], msg['Text']), msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login(True, enableCmdQR=2, loginCallback=after_login, exitCallback=after_logout)
    #itchat.send('Hello, filehelper', toUserName='filehelper')
    itchat.run()

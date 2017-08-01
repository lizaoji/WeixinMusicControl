import pygame,sys
import itchat


# 第三方包通过该命令安装：pip install itchat

HELP_MSG = u'''\
欢迎使用『微信音乐遥控器』
帮助: 显示帮助
关闭: 关闭歌曲
歌名: 按照引导播放音乐
随机: 随机开始播放
下: 播放下一首
上: 播放上一首\
'''
def playMusic():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode([640, 480])
    path = 'C:\\Users\\29076\\Music\\My Love - Westlife.mp3'
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode([640, 480])
    if msg['ToUserName'] != 'filehelper':
        return
    if msg['Text'] == 'music':
        path = 'C:\\Users\\29076\\Music\\My Love - Westlife.mp3'
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    if msg['Text'] == 'stop':
        pygame.mixer.music.stop()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                return

itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run()
sys.exit()


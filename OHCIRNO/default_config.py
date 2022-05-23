"""
默认配置。

任何自定义配置都必须从此模块导入所有内容，然后设置自定义值来覆盖默认值。

例如:

from OHCIRNO.default_config import *

HOST = '0.0.0.0'
PORT = 8080
ROOTMODE = Ture
PLAYERNAME = "WUTONK"

"""
import sys
sys.path.append("FUMOEUSHOP") 
print (sys.path)

#基本设置
HOST = '127.0.0.1' #网络功能预留ip
PORT = 8080 #网络功能预留端口
PLAYNAME = 'player' #玩家名
ROOTMODE = True #ROOT模式
TESEMODE = True #测试模式
SYSOS = 'MACOS' #运行系统

# GUI属性
GUI_SIZE = 100*100 #界面尺寸
AVATAR = "" #预留头像地址
TRANSITION_ANIMATION = True #过渡动画

#玩家初始属性
MONEY = 500
SHOP_STARS = 1 #商店星级
RENOWN = 1 #知名度

#存档位置
SAVE_FILE = '/save/save_01/'
CSV_FUMO_LIST_NAME = '/fumo_list.csv'
CSV_FILE = '/config_save.csv'
LOG_FILE = '/log.txt'

PUBLIC_FILE = 'src/public/' #公共资源库
MEDIA_FILE =  'src/public/media/' #多媒体资源库
MOVIE_FILE = '/movie'
MUSIC_FILE = '/music'
IMG_FILE = '/img'

#全局根目录



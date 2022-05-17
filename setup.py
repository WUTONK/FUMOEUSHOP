#启动设置

import OHCIRNO
from OHCIRNO import default_config
import config

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
SAVE_FILE = '/src/FUMOSHOP/playersaves'
CSV_FUMO_LIST_NAME = '/fumo_list.csv'
CSV_FILE = '/config_save.csv'
LOG_FILE = '/log.txt'
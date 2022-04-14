"""
默认配置。

任何自定义配置都必须从此模块导入所有内容，然后设置自定义值来覆盖默认值。

例如:

```python
from OHCIRNO.default_config import *

HOST = '0.0.0.0'
PORT = 8080
ROOTMODE = Ture
PLAYERNAME = "WUTONK"
```

"""

import platform

#基本设置
HOST = '0.0.0.0' #网络功能预留ip
PORT = 8080 #网络功能预留端口
PLAYNAME = 'player' #玩家名
ROOTMODE = False #ROOT模式
TESEMODE = False #测试模式
SYSOS = 'MACOS' #运行系统

# GUI功能
GUI_SIZE = 100*100 #界面尺寸
AVATAR = "" #预留头像地址
TRANSITION_ANIMATION = False #过渡动画

#玩家初始属性
MONEY = 500
SHOP_STARS = 1 #商店星级
RENOWN = 1 #知名度



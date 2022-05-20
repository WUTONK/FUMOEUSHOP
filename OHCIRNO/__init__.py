from email.policy import default
import os
import re
import linecache
import json
import shutil
import pandas
import jieba
import sys
import platform
import webbrowser
#上面是将常用模块直接引用，不用在各个文件里逐个引用
print("")
sys.path.append('')

__version__ = (0, 0, 1)

from SHOP import shops as shops
from default_config import *

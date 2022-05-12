import os
from tkinter.tix import Form
from wsgiref.util import shift_path_info
import pandas
from OHCIRNO import default_config

class shopinit:

    def shopinit(self):
        self.Define_file_location()
        self.print_debug_information()

    def shopinit_variable():
        module_path = ''

    def Define_file_location():
         #定义文件位置
        module_path = os.path.dirname(__file__)    
        filename = module_path + '/test.txt'
        fumoCsvFlie = default_config.SAVE_FILE + '/fumoshoplist'

        #检测csv文件是否存在

        #打开fumo在售列表
        fumoShopCsv = pandas.read_csv(fumoCsvFlie)
        fumo_namelist = list(fumoShopCsv.iloc[:, 0]) #取第一列的转为fumonamelist
        fumo_moneylist = list(fumoShopCsv.iloc[:, 1])

        return fumoCsvFlie,fumo_namelist,fumo_moneylist

    def Define_fumo_num_namelist(fumo_namelist):
        fumoNumNamelist = []#初始化
        i = 0
        a = len(fumo_namelist)
        while i!=a:
            fumoNumNamelist.append(str(i)+"."+fumo_namelist[i]+"("+str(fumo_moneylist[i])+")")#将索引值加上符号，名称
            list(fumoNumNamelist)
            i += 1
        
        return fumoNumNamelist,module_path,filename,fumoCsvFlie,fumoShopCsv

    def print_debug_information(fumo_namelist):

        #调试信息显示
        print(fumoNumNamelist)
        print("_________________页面01（shopinit）,调试信息：")
        print(fumoShopCsv,fumo_moneylist,fumo_namelist)
        print("_________________初始化结束_________________")

        return fumoNumNamelist,module_path,filename,fumoCsvFlie,fumoShopCsv
    
class shop_GUI:
    pass
import sys
from typing_extensions import Self
sys.path.append('../OHCIRNO')#添加加载路径，不然找不到包
from OHCIRNO import os,re,linecache,json,shutil,pandas
import OHCIRNO
import player_attribute

#入口
def main():
    maincls = mainclass()
    shop = fumoshop()
    maincls.swithviews()

#负责主控功能
class mainclass(object):

    def __init__(self):
        self.money = 1145
        self.fumosave_list = []

    def swithviews(self):

        print("正在初始化...调试信息：")
        fumoshop.init() # 初始化
        print("正常")
        while True:
            swithView = str(input("要进入的页面："))
            
            if swithView == '1':
                fumoshop.shopinit()
            if swithView == '2':
                player_attribute.saves.fumoWarehouse(fumosave_type=3,fumoname="流汗黄豆",fumonum = 90)
    
class saves():
    
    #fumo仓库函数，负责存储fumo列表和添加删除功能
    pass

#负责商店功能
class fumoshop(object):

    def __init__(self):
        super().__init__()
        self.money = 1145 #金钱
        self.sc = 14
        ShopStars = 1 #商店星级
        renown = 10 #知名度

    def shopinit():

        global fumo_namelist,fumoNumNamelist,\
        module_path,filename,fumoCsvFlie,fumoShopCsv

        fumo_namelist,fumoNumNamelist,module_path,filename,fumoCsvFlie,fumoShopCsv\
        = OHCIRNO.shops.shopinit()#从OHCIRON加载初始化


    def findfumo(self,fumoName):
        
       

        for fumos in fumo_namelist:
            if fumoName == fumo_namelist:
                # 获得对应fumo在列表中的索引
                index = fumo_namelist.index(fumoName)
                print("找到fumo！索引为：",index)
                return index
        else:
            print("输入有误，请重新输入！")
            return 0


    def reputation():
        """
        负责商店的声誉评价功能
        """    

    def propaganda():
        """
        负责商店的宣传功能
        """
        print("请选择宣传类型：")
        print("1.社区广告 2.社交媒体广告 3.视频广告")
        

    def subMoney():
        """
        金钱计算
        """
        pass
        
    def bayfumo():
        wantbuy = str(print("仓库内的fumo有：",fumoNumNamelist,"请选择要购买的fumo:"))

class shop_gui(Self):
    def __init__(self):
        pass

class player(object):
    pass


class staff(object):
    """
    员工类
    """
    def __init__(self):
        staffAmount = 0 #员工数量
        sraffWages = 0 #员工工资（0-30000€）
        staffAbility_converse = 0 #员工交谈能力（0-200）
        staffAbility_speed = 0 #员工速度（0-200）
        staffAbility_promote = 0 #推销能力（0-200）
        staffProductivity = 0 #员工效率（0-300%）
        pass

    def staffBehavior():
        """
        员工行为：效率，星级，满意度管理
        """
        pass

    def personnel():
        """
        人事管理
        """
        pass

    def wages():
        """
        员工薪酬处理
        """
        pass

    def AutoSales():
        """
        员工自动销售处理
        """
        pass

class TimeSelley(object):
    """
    负责与时间计算程序对接
    """
    def __init__(self):
        pass
    


if __name__ == "__main__":
    main()


    





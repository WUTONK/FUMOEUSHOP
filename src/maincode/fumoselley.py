import os
from posixpath import split
import re
import linecache
import json
import shutil
from unicodedata import name
import pandas
from pyparsing import withClass

"""

//_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
//                                                                                                                       
//                                     欢迎进入源代码页面！━(*｀∀´*)ノ亻!                                                                                      
//                                                                                                                       
//                                      项目：FUMOEUSHOP                                                                                  
//                                      版本：alpha v.0.0.0                                                                         
//                                      开发者：WUTONK                                                                            
//                                      开始日期：2021-12-13   
//                                      最后编辑日期：2021-2-5
//                                      本页面功能：主页以及游戏逻辑运行                                                                              
//                                                                                                                                                                                                           
//                                                      ┌      ┐ 
//												          ' 」'      welcome to the code                                                 
//                                                      └  ︶  ┘                                     
//                                                                                
//_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

"""

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
        fumoshop.shopinit() # 初始化
        print("正常")
        while True:
            swithView = str(input("要进入的页面："))
            
            if swithView == '1':
                fumoshop.shopinit()
            if swithView == '2':
                self.saves.fumoWarehouse(fumosave_type=3,fumoname="流汗黄豆",fumonum = 90)
    
    class saves():
        
        #fumo仓库函数，负责存储fumo列表和添加删除功能
        def fumoWarehouse(fumosave_type,fumoname,fumonum):
    
            print("_______________页面02（fumoWarehouse）,调试信息：")

            #读取csv文件
            WarehouselistScvFlie = './myfumolist_csv.csv'
            WarehouselistScv = pandas.read_csv(WarehouselistScvFlie)
            WarehouseFumoList = list(WarehouselistScv.iloc[:, 0]) #读取位于name行的数据
            WarehouseFumonumList = list(WarehouselistScv.iloc[:, 1])

            print("文件读取完毕")
            print(WarehouselistScv)

            #存储模式
            if fumosave_type == 1:
                print("打开了存储模式")
                
                #检测fumo是否存在
                for fumos in WarehouseFumoList:
                    if fumos == fumoname:
                        # 获得对应fumo在列表中的索引
                        index = WarehouseFumoList.index(fumoname)
                        print("这个fumo已经在仓库里了！索引为：",index)
                        break
                #fumo不存在的处理逻辑 
                else:  
                        data = {'name':[fumoname],'quantity':[fumonum]}
                        data_1 = pandas.DataFrame(data)
                        data_1.to_csv(WarehouselistScvFlie, mode='a',index=False, header=False) #以追加模式写入
                        

            #第一删除模式（清空仓库中的某个fumo的所有存货）
            if fumosave_type == 2:
                for fumos in WarehouseFumoList:
                    if fumos == fumoname:
                        # 获得对应fumo在列表中的索引
                        del_index = WarehouseFumoList.index(fumoname)
                        WarehouselistScv_del =WarehouselistScv.drop(del_index) #把指定行删除，vscode不知道为啥不给drop提示
                        print(WarehouselistScv_del)
                        WarehouselistScv_del.to_csv(WarehouselistScvFlie,index=False,encoding="utf-8")#删除后保存
                        break    
            #第二删除模式（修改某行的fumo数量）
            if fumosave_type == 3:
                    
                    # 开始查找fumoname行
                    for fumos in WarehouseFumoList:
                        if fumos == fumoname:
                            # 获得对应fumo在列表中的索引
                            index = WarehouseFumoList.index(fumoname)

                    fumoQuantityNums= list(WarehouselistScv.iloc[index:, 1])[0]
                    print(fumoQuantityNums)

                    #开始计算，然后转字符串写入
                    fumonum = int(fumonum)
                    
                    print(fumonum,fumoQuantityNums)
                    if fumonum >= 0:
                        fumoQuantityNums = (fumoQuantityNums+fumonum) #fumonum即为外部传入的fumo数量
                    elif fumonum <0:
                        fumoQuantityNums = (fumoQuantityNums-fumonum)
                    else:
                        print("fumonums全局变量错误，值为：",fumonum)
                    

                    #写入 
                    Warehouselist = WarehouselistScv.to_dict()#转列表
                    print(Warehouselist)
                    Warehouselist['quantity'][index] = fumoQuantityNums
                    print(Warehouselist)
                    Warehouselist = pandas.DataFrame(Warehouselist)
                    Warehouselist.to_csv(WarehouselistScvFlie,index=False)
                    print(Warehouselist)

        #普通存档功能
        def playersave_1(money,shopStars,reown):
            pass
        
        #存档备份功能
        def playersave_2(saveFile):

            newFilenName = saveFile+"_copy"
            os.mkdir(newFilenName)
            shutil.copyfile(saveFile, newFilenName)
            "{}{}{}".format(saveFile,"已经复制到",newFilenName)
            
            
        #存档删除功能
        def playersave_3(removeSaveName):
            os.remove(removeSaveName)
            "{}{}{}".format("存档",removeSaveName,"已删除！")

        #新建存档功能
        def playersave_4(money,shopStars,reown):
            
            fileExistence = True
            #查找文件是否存在
            for savenum in range(101):
                fileExistence = os.path.exists("./playsaves/save_"+ str(savenum))
                if fileExistence == False:
                    newFilenName = "./playsaves/save_"+ str(savenum+1)
                    break
            #新建存档文件夹
            

        #存档调试功能（开发者用）
        def playersave_5(money,shopStars,reown):
            pass

        #存档损坏处理
        def playersave_6():
            pass


class mainView:
    def __init__(self) :
        pass

#负责商店功能
class fumoshop(object):

    def __init__(self):
        super().__init__()
        self.money = 1145 #金钱
        self.sc = 14
        ShopStars = 1 #商店星级
        renown = 10 #知名度

    #商店初始化变量
    def shopinit():

        #设定全局变量
        global fumo_namelist
        global fumo_moneylist
        global fumoNumNamelist

        #打开fumo在售列表
        
        fumoShopCsv = pandas.read_csv('./fumoshoplist_csv.csv')
        fumo_namelist = list(fumoShopCsv.iloc[:, 0]) #取第一列的转为fumonamelist
        fumo_moneylist = list(fumoShopCsv.iloc[:, 1])

        #计算全局变量
        fumoNumNamelist = []#初始化
        b = 0
        a = len(fumo_namelist)
        while b!=a:
            fumoNumNamelist.append(str(b)+"."+fumo_namelist[b]+"("+str(fumo_moneylist[b])+")")#将索引值加上符号，名称
            list(fumoNumNamelist)
            b = b+1

        #调试信息显示
        print(fumoNumNamelist)
        print("_________________页面01（shopinit）,调试信息：")
        print(fumoShopCsv,fumo_moneylist,fumo_namelist)
        print("_________________初始化结束_________________")

        return #将计算出的变量返回


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

class player(object):
    pass

class FileReads(object):
    """
    读取文件的统一类
    """
    def __init__(self):
       pass

class staff(object):
    """
    员工类
    """
    def __init__(self):
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


    





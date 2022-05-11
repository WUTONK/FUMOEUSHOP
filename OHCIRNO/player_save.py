"""
负责存档
"""

import sys,os,re,linecache,json,shutil,pandas

import OHCIRNO

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
                fumoWarehouse(fumosave_type=3,fumoname="流汗黄豆",fumonum = 90)
    
class saves():
    def __init__(self):
        save_file = '' #存档路径
        save_name = '' #要使用的存档名


    #fumo仓库函数，负责存储fumo列表和添加删除功能
    def save(fumosave_type,fumoname,fumonum,WarehouselistScvFlie):

        print("_______________页面02（fumoWarehouse）,调试信息：")

        #读取csv文件
        WarehouselistScv = pandas.read_csv(WarehouselistScvFlie)
        WarehouseFumoList = list(WarehouselistScv.iloc[:, 0]) #读取位于name行的所有数据
        WarehouseFumonumList = list(WarehouselistScv.iloc[:, 1]) #读取位于num行的所有数据

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
                    

        #删除模式（清空仓库中的某个fumo的所有存货）
        if fumosave_type == 2:
            for fumos in WarehouseFumoList:
                if fumos == fumoname:
                    # 获得对应fumo在列表中的索引
                    del_index = WarehouseFumoList.index(fumoname)
                    WarehouselistScv_del =WarehouselistScv.drop(del_index) #把指定行删除，vscode不知道为啥不给drop提示
                    print(WarehouselistScv_del)
                    WarehouselistScv_del.to_csv(WarehouselistScvFlie,index=False,encoding="utf-8")#删除后保存
                    break    
        #修改模式（修改某行的fumo数量）
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
                Warehouselist = WarehouselistScv.to_dict()#转字典
                Warehouselist['quantity'][index] = fumoQuantityNums #覆盖数量
                print("数量已经修改：",Warehouselist)
                Warehouselist = pandas.DataFrame(Warehouselist) #转dataFrame类型
                Warehouselist.to_csv(WarehouselistScvFlie,index=False) #以无索引模式写入

    #普通存档功能
    def playersave_1(saveFile):
        print("正在存储位于：",saveFile,"的存档")
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
        #循环查找文件名是否存在（被占用）
        for savenum in range(101):
            fileExistence = os.path.exists("./playsaves/save_"+ str(savenum))
            if fileExistence == False:
                newFilenName = "./playsaves/save_"+ str(savenum+1) 
                break
        #有空位，新建存档文件夹

        

    #存档调试功能（开发者用）
    def playersave_5(money,shopStars,reown):
        pass

    #存档损坏处理
    def playersave_6():
        pass

    





"""
负责存档
"""

import sys
import os
import re
import linecache
import json
import shutil
import pandas

import OHCIRNO
from OHCIRNO import shops

#负责主控功能

class mainclass(object):

    def __init__(self):
        self.money = 1145
        self.fumosave_list = []

    def swithviews(self):

        print("正在初始化...调试信息：")
        OHCIRNO.shops  # 初始化
        print("正常")
        while True:
            swithView = str(input("要进入的页面："))

            if swithView == '1':
                fumoshop.shopinit()
            if swithView == '2':
                saves.save_csv_fumo_selley(fumosave_type=3, fumoname="流汗黄豆", fumo_num=90)


class saves():
    def __init__(self):
        save_file = ''  # 存档路径
        save_name = ''  # 要使用的存档名

    def set_file():
        pass

    #fumo仓库函数，负责存储fumo列表和添加删除功能
    class save_csv_fumo_selley(fumosave_type, fumoname, fumo_num, Scv_Flie):

        #读取csv文件
        csv_warehouse = pandas.read_csv(Scv_Flie)
        csv_FumoList = list(csv_warehouse.iloc[:, 0])  # 读取位于name行的所有数据
        WarehouseFumonumList = list(
            csv_warehouse.iloc[:, 1])  # 读取位于num行的所有数据
        
        def backups(Scv_Flie):
            """
            备份csv
            """
            pass
        
        def find_index(csv_FumoList,fumoname):
            """
            寻找索引
            """
            #检测fumo是否存在
            for fumos in csv_FumoList:
                if fumos == fumoname:
                    # 获得对应fumo在列表中的索引
                    index = csv_FumoList.index(fumoname)
                    return index
                else:
                    return None

        def fumosave_type(Scv_Flie,fumoname):
            """
            以追加模式写入
            """
            data = {'name': [fumoname], 'quantity': [fumo_num]}
            data_1 = pandas.DataFrame(data)
            data_1.to_csv(Scv_Flie, mode='a',
                            index=False, header=False)  # 以追加模式写入

        def fumosave_type (csv_FumoList,csv_warehouse,Scv_Flie,fumoname):
            """
            删除模式（清空仓库中的某个fumo的所有存货）
            """
            for fumos in csv_FumoList:
                if fumos == fumoname:
                    # 获得对应fumo在列表中的索引
                    del_index = csv_FumoList.index(fumoname)
                    csv_del = csv_warehouse.drop(
                        del_index)  # 把指定行删除
                    print(csv_del)
                    csv_del.to_csv(
                        Scv_Flie, index=False, encoding="utf-8")  # 删除后保存

        def fumosave_type (csv_FumoList,csv_warehouse,Scv_Flie,fumoname):
            """
            修改模式（修改某行的fumo数量
            """
            # 开始查找fumoname
            for fumos in csv_FumoList:
                if fumos == fumoname:
                    # 获得对应fumo在列表中的索引
                    index = csv_FumoList.index(fumoname)
                else:
                    return None #找不到索引
    
            fumo_Quantity_Nums = list(csv_warehouse.iloc[index:, 1])[0]
            print(fumo_Quantity_Nums)
            #开始计算，然后转字符串写入
            fumo_num = int(fumo_num)

            print(fumo_num, fumo_Quantity_Nums)
            if fumo_num >= 0:
                fumo_Quantity_Nums = (fumo_Quantity_Nums+fumo_num)  # fumo_num即为外部传入的fumo数量
            elif fumo_num < 0:
                fumo_Quantity_Nums = (fumo_Quantity_Nums-fumo_num) 
            else:
                print("fumo_nums全局变量错误，值为：", fumo_num)

            #写入
            Warehouselist = csv_warehouse.to_dict()  # 转字典
            Warehouselist['quantity'][index] = fumo_Quantity_Nums  # 覆盖数量
            Warehouselist = pandas.DataFrame(Warehouselist)  # 转dataFrame类型
            Warehouselist.to_csv(Scv_Flie, index=False) #以无索引模式写入

    class player_save():

        #普通存档功能
        class save_normal(saveFile):
            print("正在存储位于：", saveFile,"的存档")
            pass

        #存档备份功能
        def save_backup(saveFile):

            newFilenName = saveFile+"_copy"
            os.mkdir(newFilenName)
            shutil.copyfile(saveFile, newFilenName)
            "{}{}{}".format(saveFile, "已经复制到",newFilenName)

        #存档删除功能
        class save_del(remove_Save_file):
            os.remove(remove_Save_file)
            "{}{}{}".format("存档", remove_Save_file ,"已删除！")

        #新建存档功能
        def save_new(money, shopStars,reown):

            fileExistence = True
            #循环查找文件名是否存在（被占用）
            
            #有空位，新建存档文件夹

        #存档调试功能（开发者用）
        def save_root(money, shopStars,reown):
            pass

        #存档损坏处理
        def save_damage():
            pass
    
    class save_package():
        pass

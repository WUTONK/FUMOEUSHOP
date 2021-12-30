import os
from posixpath import split
import re
import linecache

"""

//_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
//                                                                                                                       
//                                     欢迎进入源代码页面！━(*｀∀´*)ノ亻!                                                                                      
//                                                                                                                       
//                                      项目：FUMOEUSHOP                                                                                  
//                                      版本：alpha v.0.0.0                                                                         
//                                      开发者：WUTONK                                                                            
//                                      开始日期：2021-12-13   
//                                      最后编辑日期：2021-12-31
//                                      本页面功能：主页以及游戏逻辑运行                                                                              
//                                                                                                                                                                                                           
//                                                      ┌      ┐ 
//												          ' 」'      welcome to the code                                                 
//                                                      └  ︶  ┘                                     
//                                                                                
//_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

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
                self.fumoWarehouse(fumosave_type=3,fumoname="我超恶俗啊",fumonum = 90)
    
    class saves():
        
        #fumo仓库函数，负责存储fumo列表和添加删除功能
        def fumoWarehouse(self,fumosave_type,fumoname,fumonum):

            print("_______________页面02（fumoWarehouse）,调试信息：")
            #读取文件
            with open("./myfumolist", "r+") as fumosave_file:
                fumos_data = fumosave_file.read()
                fumos_list = fumos_data.split("\n")
                print("文件读取完毕")
                print(fumos_list)

                #存储模式
                if fumosave_type == 1:
                    print("打开了存储模式")

                    for fumos in fumos_list:
                        if fumos == fumoname:
                            # 获得对应fumo在列表中的索引
                            index = fumos_list.index(fumoname)
                            print("这个fumo已经在仓库里了！索引为：",index)
                            return 
                    else:  
                        with open("./myfumolist", "a") as fumosave_file:
                            print(fumoname)   
                            fumosave_file.write(fumoname + "\n" + "x" + str(fumonum) + "\n" )
                            fumosave_file.close()

                #第一删除模式（清空仓库中的某个fumo的所有存货）
                if fumosave_type == 2:
                    with open("./myfumolist", "w") as fumosave_file:
                        print("打开了第一删除模式")#下一行：通过find()函数找到包含要删除内容的行数    
                        lines = [cirno for cirno in open("myfumolist", "r") if cirno.find(fumoname) != 0]
                        print(lines)
                        fd = open("myfumolist", "w")
                        fd.writelines(lines)
                        return        
                #第二删除模式（修改某行的fumo数量）
                if fumosave_type == 3:
                    with open("./myfumolist", "r") as fumosave_file:
                        print("打开了第二删除模式")
                        string = str(fumoname)
                        

                        # 开始查找fumoname行
                        count = 0
                        fumosave_file = open('./myfumolist', "r+")
                        for line in fumosave_file.readlines():
                            if string in line:
                                print("第 "+str(count)+" 行已找到.")
                                print("该行内容: \n"+line)
                                break #如果已经找到了就跳出循环，不然名字部分重合就会出bug，虽然现在还是会，艹
                            count += 1
                            countnext = count #用来存储下一行的行数
                        fumosave_file.close()

                        fumonums = linecache.getline('./myfumolist', countnext)
                        fumonums = fumonums.replace("x",'') #将'x'去除，不然转换不了int类型
                        fumoname = str(line)
                        print("fumonums:",fumonums,"fumoname:",fumoname)

                        #开始计算，然后转字符串写入
                        fumonum = int(fumonum)
                        fumonums = int(fumonums)
                        print(fumonum,fumonums)
                        if fumonum >= 0:
                            fumonums = (fumonums+fumonum) #fumonum即为外部传入的fumo数量
                        elif fumonum <0:
                            fumonums = (fumonums-fumonum)
                        else:
                            print("fumonums全局变量错误，值为：",fumonum)
                        print()

                        #写入 
                        with open("./myfumolist", "r") as fumosave_file:
                            line_to_replace = countnext #选取要写入的行数
                            lines = fumosave_file.readlines()
                        #now we have an array of lines. If we want to edit the line 17...
                        if len(lines) > int(line_to_replace):
                            lines[line_to_replace] = ('x'+fumonums)

                        with open("./myfumolist",'w') as fumosave_file:
                            fumosave_file.writelines(lines)
                            fumosave_file.close()

        #普通存档功能
        def playersave_1(money,shopStars,reown):
            pass
        
        #存档备份功能
        def playersave_2(money,shopStars,reown):
            pass

        #存档删除功能
        def playersave_3(money,shopStars,reown):
            pass

        #新建存档功能
        def playersave_4(money,shopStars,reown):
            pass
        
        #存档调试功能（开发者用）
        def playersave_5(money,shopStars,reown):
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
        with open('./fumoshoplist', 'r', encoding='utf-8') as fumo_data:
            fumo_data = fumo_data.read()
        fumo_list = fumo_data.split("\n")
        try:
            fumo_list.remove("") #如果文件里有空格就删除
        except:
            pass

        #计算全局变量
        fumo_namelist = fumo_list[1::2] #从1开始，取步长为2的值，即奇数（fumo的价格在列表的位置）
        fumo_moneylist = fumo_list[::2] #取步长为2的值，即偶数（fumo的名字在列表的位置）
        fumoNumNamelist = []#初始化
        b = 0
        a = len(fumo_namelist)
        print(a)
        while b!=a:
            fumoNumNamelist.append(str(b)+"."+fumo_namelist[b]+"("+fumo_moneylist[b]+")")#将索引值加上符号，名称
            list(fumoNumNamelist)
            b = b+1

        #调试信息显示
        print(fumoNumNamelist)
        print("_________________页面01（shopinit）,调试信息：")
        print(fumo_list,fumo_moneylist,fumo_namelist)
        print("_________________初始化结束_________________")

        return #将计算出的变量返回


    def findfumo(self,fumoName):
        for fumos in fumo_namelist:
            if fumoName == fumo_namelist:
                # 获得对应fumo在列表中的索引
                index = fumo_namelist.index(fumoName)
                return "找到fumo！索引为：",index
        else:
            return "输入有误，请重新输入！"


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
        pass
        
    def bayfumo():
        wantbuy = str(print("仓库内的fumo有：",fumoNumNamelist,"请选择要购买的fumo:"))

class player(object):
    pass

if __name__ == "__main__":
    main()


    





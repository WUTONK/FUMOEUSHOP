import os
import pandas

class shopinit:
    def shopinit_variable():
        module_path = ''

    def shopinit():

         #定义文件位置
        module_path = os.path.dirname(__file__)    
        filename = module_path + '/test.txt'
        fumoCsvFlie = './fumoshoplist_csv.csv'
    

        #打开fumo在售列表
        fumoShopCsv = pandas.read_csv(fumoCsvFlie)
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

        return fumo_namelist,fumoNumNamelist,module_path,filename,fumoCsvFlie,fumoShopCsv
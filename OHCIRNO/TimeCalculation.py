"""
总时间处理
"""

import time

class time_get(object):   
    """
    获取时间
    """

    def __init__(self):
       pass

    def get_system_time():
        """
        获取系统时间，返回yy,mm,dd,hh,ss
        """
        t = time.localtime()
        time_local = [t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec]
        return time_local

    def get_time_格式化 ():
        """
        时间格式化
        """
        return_time = ''

        time_local = time_get.get_system_time()

        get_time_ = [time_local]

        for i in range(get_time_):
            if get_time_[i] != None:
                return_time += str(get_time_[i])+':'
        
        return return_time.strip(':')#将结尾的':'去除
        
class time_save_read(object):

    def time_save_read():
        """
        存取时间
        """    

class Statistical(object):

    def Statistical_game_time():
        """
        统计时间
        """
        pass

    def time_ ():
        """
        计时剩余时间计算
        """

"""
检测用户系统配置等
"""
import platform
import sys
import os

class sys_Detection():

    def Detection_all(self):
        sys_name = self.sys_testing()
        bool_64 = self.detection_64()

        return sys_name,bool_64

    def sys_testing():
        if platform.system().lower() == 'windows':
            return 'windows'
        elif platform.system().lower() == 'linux':
            return 'linux'
        elif platform.system().lower() == 'darwin':
            return 'macos' 
    def detection_64():
        """
        检测系统是否为64位
        """
        maxbit = sys.maxsize

        if maxbit>2**32:
            return True #为64位系统
        else:
            return False

    
    


        
            
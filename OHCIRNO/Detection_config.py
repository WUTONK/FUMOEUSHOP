"""
检测用户系统配置等
"""
import platform
import sys
import os

class sys_Detection():
    def sys_testing():
        if platform.system().lower() == 'windows':
            return 'windows'
        elif platform.system().lower() == 'linux':
            return 'linux'
        elif platform.system().lower() == 'darwin':
            return 'macos' 
    def Detection_64():
        if:
            return True
        else:
            return False


        
            
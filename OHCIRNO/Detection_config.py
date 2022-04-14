"""
检测用户系统配置等
"""
import platform
import sys
import os

print(os.name)
print("111")
class sys_config():
    def sys_testing():
        if platform.system().lower() == 'windows':
            return 'windows'
        elif platform.system().lower() == 'linux':
            return 'linux'
        elif platform.system().lower() == 'darwin':
            return 'macos'

        
            
from pathlib import Path
import os

"""
def get_project_root() -> Path:
    #返回../../../根目录
    return Path(__file__).parent.parent.parent
"""
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)
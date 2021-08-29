"""
python 统计文件夹下各个子目录中的文件个数
"""
import os

for dirpath, dirnames, filenames in os.walk("D:\yueyue\pythontest\learn_python"):
    file_count = 0
    for file in filenames:
        file_count += 1
    print(dirpath, file_count)

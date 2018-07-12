# -*- coding: UTF-8 -*-
import threading
import os
import sys
import codecs
import re
import time
import math
from sys import argv

if len(argv) != 4:
        exit('usage: python split_file.py <num_of_threads> <input_file_path> <tmp_dir>')
k, input_file, tmp_dir = argv[1:]
if not os.path.exists(input_file):
        exit('input_file_path does not exist.')

k = int(k)

if not os.path.exists(tmp_dir):
        os.system('mkdir ' + tmp_dir)
# 生成中间输入文件
with codecs.open(input_file, 'r', 'utf-8') as fid:
        lines = fid.read().strip().split('\n')
n = len(lines)
m = int(math.ceil( n / float(k)))
for i in range(k):
        writer = codecs.open(tmp_dir+str(i)+'.txt', 'w', 'utf-8')
        for j in range(m):
                if i*m + j >= n:
                        break
                writer.write(lines[i*m + j]+'\n')
        writer.close()
print('input file already splited >>>')

# -*- coding: UTF-8 -*-
import threading
import os
import sys
import codecs
import re
import time
import math
from sys import argv
#from subprocess import call
#threading_namespace = threading.local() # 命名空间

def run_cpp(cpp_name, model_path, input_file, output_file):
        my_cmd = cpp_name + ' ' + model_path + ' ' + input_file + ' ' + output_file
        os.system(my_cmd)

if len(argv) != 7:
        exit('usage: python multi_thread_test.py <tmp_dir> <num_of_thread> <cpp_name> <model_path> <input_file_path> <output_file_dir>')
tmp_dir, k, cpp_name, model_path, input_file, output_dir = argv[1:]
if not os.path.exists(tmp_dir):
        exit('tmp_dir does not exist.')
if not os.path.exists(output_dir):
	os.system('mkdir '+output_dir)
if not os.path.exists(input_file):
        exit('input_file_path does not exist.')

k = int(k)

if os.path.exists(output_dir):
        os.system('rm -r '+output_dir)
        os.system('mkdir '+output_dir)
# 停留5秒让文件分割完成
#time.sleep(5)

# 开始多线程运行程序
threads = []
for i in range(k):
    threads.append(threading.Thread(target=run_cpp,args=(cpp_name, model_path, tmp_dir+str(i)+'.txt', output_dir+str(i)+'.txt')))

for t in threads:
    t.start()

for t in threads:
    t.join()

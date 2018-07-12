import os
import sys
import codecs
import random

if __name__ == '__main__':
    input_dir = '/cephfs/share/data/new_names/'
    output_file = '/cephfs/share/data/zhancheng/zhou/names_all.txt'
    writer = codecs.open(output_file, 'w','utf-8')
    for txt_name in os.listdir(input_dir):
        input_file = input_dir + txt_name
        with codecs.open(input_file, 'r','utf-8') as fid:
                if txt_name == 'cat.txt' or txt_name == 'dog.txt':
                        lines = fid.read().strip().split('\n')
                        random.shuffle(lines)
                        for i in range(1000):
                                writer.write(lines[i]+'\n')
                else:
                        writer.write(fid.read())
    writer.close()

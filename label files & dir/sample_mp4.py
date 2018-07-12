#-*- coding:utf-8 -*-
import os
import sys
import codecs
import random
import re

def get_list(t_file):
        t_list = []
        with codecs.open(t_file, 'r', 'utf-8') as fid:
                for line in fid.read().strip().split('\n'):
                        t_list.append(line.split(' ')[0])
        return t_list

def make_dirs(output_dir, t_list):
        for i in range(len(t_list)):
                os.system('mkdir '+output_dir+str(i+1))

def neaten_files(input_file, output_file):
        i = 0
        writer = codecs.open(output_file, 'w', 'utf-8')
        with codecs.open(input_file, 'r', 'utf-8') as fid:
                lines = fid.read().strip().split('\n')
                random.shuffle(lines)
                for line in lines:
                        if len(line.split(' ')) < 2:
                                continue
                        mp4_path = line.split(' ')[0]
                        labels = line.split(' ')[1]
                        if u'自拍' in labels:
                                writer.write('http://100.115.5.36/' + mp4_path.split('/')[-1].rstrip('.mp4')+'.f0.mp4' + '\n')
                                i += 1
                                if i >= 500:
                                        break

if __name__ == '__main__':
        input_file = '/cephfs/share/data/zipai_all.txt'
        output_file = '/cephfs/share/data/zipai_sample_500.txt'
        #if not os.path.exists(output_dir):
        #        os.system('mkdir '+output_dir)
        #target_file = ''
        neaten_files(input_file, output_file)

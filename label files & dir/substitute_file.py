#-*- coding:utf-8 -*-
import os
import sys
import codecs
import re

def easy_subst(input_file, output_file, subst, target):
        writer = codecs.open(output_file, 'w', 'utf-8')
        with codecs.open(input_file, 'r', 'utf-8') as fid:
                for line in fid.read().strip().split('\n'):
                        flag = 0
                        for t in target:
                                if t in line:
                                        writer.write(line.split(' ')[0] + ' ' + subst + '\n')
                                        flag = 1
                                        break
                        if flag == 0:
                                writer.write(line.split(' ')[0] +' '+ u'其它' +'\n')

if __name__ == '__main__':
        input_file = '/cephfs/darnellzhou/VideoClassify/tmp_groundtruth/2018-06-23-2018-06-28_tmp_gdtruth.txt'
        output_file = '/cephfs/darnellzhou/VTalentDetect/new_gdtruth.txt'
        subst = u'才艺'
        target = [u'才艺', u'生活随拍']
        easy_subst(input_file, output_file, subst, target)

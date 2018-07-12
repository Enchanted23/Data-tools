#-*- coding:utf-8 -*-
import os
import sys
import codecs
import re

def get_label_list(input_file, output_file):
	label_list = []
	with codecs.open(input_file, 'r', 'utf-8') as fid:  
		for line in fid.read().strip().split('\n'):
			labels = line.split(' ')[1].split(',')
			for label in labels:
				if not label in label_list:
					label_list.append(label)
	label_list.sort()
	writer = codecs.open(output_file, 'w', 'utf-8')
	for label in label_list:
		writer.write(label+'\t'+'\n')
	writer.close()

if __name__ == '__main__':
	input_file = '/cephfs/group/youtu/data/OpenSourceDetData/category_anlysis/58_obj_check_erhu.txt'
	output_file = '/cephfs/share/data/zhancheng/zhou/org_label.txt'
	get_label_list(input_file, output_file)
